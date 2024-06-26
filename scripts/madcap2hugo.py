import re
import os
import sys
import json
import requests
import argparse
import pypandoc
from urllib.parse import urljoin
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup


def combine_urls(base_url, relative_url):
    return urljoin(base_url, relative_url)


def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None

def extract_define_content(data):
    if isinstance(data, bytes):
        data = data.decode('utf-8')
    match = re.search(r'define\((.*)\);', data)
    if match:
        json_str = match.group(1)
        json_str = re.sub(r'(\w+):', r'"\1":', json_str)
        json_str = re.sub(r"'", '"', json_str)

        try:
            parsed_data = json.loads(json_str)
            return parsed_data
        except json.JSONDecodeError as e:
            print(f"Decode error JSON: {e}")
            return None
    else:
        return None

def get_xml_attr(xml_content, attr_name):
    if xml_content:
        tree = ET.ElementTree(ET.fromstring(xml_content))
        root = tree.getroot()
        if root is not None:
            attr_value = root.attrib.get(attr_name)
            return attr_value
    return None


def get_desc_menu_by_id(desc_menu, id):
    for url, data in desc_menu.items():
        if data.get('i') == [id]:
            return ({
                'title': data['t'][0],
                'page_url': url
            })
    return None

def add_weights(data):
    def set_weight(item, weight):
        item['weight'] = weight
        if 'children' in item:
            for i, child in enumerate(item['children']):
                set_weight(child, i + 1)

    for i, item in enumerate(data):
        set_weight(item, i + 1)

    return data

def fetch_menu_structure(menu, desc_menu_list, parent_id=None, link=""):
    desc_menu = get_desc_menu_by_id(desc_menu_list, menu["i"])
    link += desc_menu["page_url"].replace('.html', '')
    menu_structure = {
        "id": menu["i"],
        "title": desc_menu["title"],
        "link": link,
        "page_url": desc_menu["page_url"],
        "parentId": parent_id
    }

    children = menu.get("n", [])
    if children:
        menu_structure["children"] = [fetch_menu_structure(child, desc_menu_list, menu["i"], link) for child in children]

    return menu_structure

def add_prefix_to_directories(path, prefix):
    parts = path.strip(os.sep).split(os.sep)
    new_parts = [f"{prefix}-{part}" for part in parts]
    new_path = os.sep.join(new_parts)
    return new_path


def get_page_html(page_url):
    response = requests.get(page_url)
    if response.status_code == 200:
        page_html = response.text
    else:
        print(f"The page isnt avaiable. Status code: {response.status_code}")
    return page_html


def get_page_main_content(soup):
    body = soup.find("div", {"id": "mc-main-content"})
    if body:
        body_text = body.decode_contents()
        page_main_content = BeautifulSoup(body_text, 'html.parser')
        return page_main_content
    else:
        return None


def convert_mctextpopup(soup):
    popup_elements = soup.find_all('a', class_='MCTextPopup')
    for element in popup_elements:
        popup_text = element.find('span', class_='MCTextPopupBody').text.strip()
        element.name = 'a'
        element['href'] = '#'
        element['title'] = popup_text
        element.string = element.contents[0].strip()
    return soup


def remove_attributes(soup):
    attributes_to_remove = ['class', 'style', 'colspan', 'rowspan', 'valign', 'data_mc_pattern']
    for attribute in attributes_to_remove:
        elements_with_attribute = soup.find_all(attrs={attribute: True})
        for element in elements_with_attribute:
            del element[attribute]
    return soup


def convert_info(soup):
    infos = soup.find_all('div', class_='note')
    if infos:
        for info in infos:
            info_html = info.decode_contents()
            hugo_shortcode = "{{{{%tip%}}}}{}{{{{%/tip%}}}}".format(info_html)
            info.replace_with(BeautifulSoup(hugo_shortcode, 'html.parser'))
    return soup

def convert_important(soup):
    importants = soup.find_all('div', class_='important')
    if importants:
        for important in importants:
            important_html = important.decode_contents()
            hugo_shortcode = "{{{{%note%}}}}{}{{{{%/note%}}}}".format(important_html)
            important.replace_with(BeautifulSoup(hugo_shortcode, 'html.parser'))
    return soup


def convert_dropdown(soup):
    dropdowns = soup.find_all('div', class_='MCDropDown')
    for dropdown in dropdowns:
        header = dropdown.find('span', class_='MCDropDownHead').get_text(strip=True)
        body = dropdown.find('div', class_='MCDropDownBody')
        if body:
            body_text = body.decode_contents()
        else:
            body_text = ''
        combined_text = BeautifulSoup(f"{header}<br>{body_text}", 'html.parser')
        dropdown.replace_with(combined_text)
    return soup


def convert_uicontrol(soup):
    for span in soup.find_all('span', class_='uicontrol'):
        span.wrap(soup.new_tag('strong'))
        span.unwrap()
    return soup

def convert_mcpopup_img(soup, url, output_dir):
    madcap_tags = soup.find_all('madcap:conditionaltext')
    if madcap_tags:
        for madcap_tag in madcap_tags:
            a_tag = madcap_tag.find('a', class_='MCPopupThumbnailLink')
            img_tag = madcap_tag.find('img', class_='MCPopupThumbnail img')
            if a_tag and img_tag:
                href = a_tag.get('href')
                href_url = combine_urls(url, href)
                href_filename = href.split('/')[-1]
                download_attachment(href_url, href_filename, output_dir)

                src = img_tag.get('src')
                src_url = combine_urls(url, src)
                src_filename = src.split('/')[-1]
                download_attachment(src_url, src_filename, output_dir)

                new_a_tag = BeautifulSoup(f'<a href="{href_filename}"><img src="{src_filename}"></a>', 'html.parser')
                madcap_tag.replace_with(new_a_tag)
    return soup


def download_attachment(url, name, path):
    full_name = os.path.join(path, name)
    r = requests.get(url)
    if r.status_code == 200:
        with open(full_name, "wb") as f:
            for bits in r.iter_content():
                f.write(bits)


def convert_madcap_html_to_md(url, page, output_dir):
    page = page.lstrip('/')
    page_url = combine_urls(url, page)
    page_html = get_page_html(page_url)
    soup = BeautifulSoup(page_html, 'html.parser')
    soup = get_page_main_content(soup)
    soup = convert_info(soup)
    soup = convert_important(soup)
    soup = convert_uicontrol(soup)
    soup = convert_dropdown(soup)
    soup = convert_mcpopup_img(soup, url, output_dir)
    soup = convert_mctextpopup(soup)

    md_content = pypandoc.convert_text(
        soup,
        format='html',
        to='gfm',
        extra_args=['--markdown-headings=atx', '--wrap=none']
    )
    return md_content


def generate_hugo_structure(data, url, output_dir, root_doc_name):
    for item in data:
        path_with_prefix = add_prefix_to_directories(item['link'][1:], root_doc_name)
        path = os.path.join(output_dir, path_with_prefix)

        if 'children' in item:
            path_with_prefix = add_prefix_to_directories(os.path.basename(item['link']), root_doc_name)
            path = os.path.join(path, path_with_prefix)
        os.makedirs(path, exist_ok=True)
        md_filename = os.path.join(path, 'index.md')

        md_content = convert_madcap_html_to_md(url, item['page_url'], path)

        identifier = root_doc_name if root_doc_name == os.path.basename(item['link']) else f"{root_doc_name}-{os.path.basename(item['link'])}"
        parent = root_doc_name if root_doc_name == os.path.basename(os.path.dirname(item['link'])) else f"{root_doc_name}-{os.path.basename(os.path.dirname(item['link']))}"

        with open(md_filename, 'w') as f:
            f.write(f'''---
draft: false
title: "{item['title']}"
aliases: "/{identifier}/"
seoindex: "index, follow"
seotitle: "{item['title']}"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "{item['title']}"
        url: "/{identifier}/"
        weight: "{item['weight']}"
        parent: "{parent if item['parentId'] else root_doc_name}"
        identifier: "{identifier}"
---

# {item['title']}

{md_content}

''')

        if 'children' in item:
            generate_hugo_structure(item['children'], output_dir, root_doc_name)


def main():
    parser = argparse.ArgumentParser(description='Extract attributes from a webpage.')
    parser.add_argument('--url', required=True, help='URL to webpage')
    parser.add_argument('--root_doc_name', required=True, help='Hugo root doc name')
    args = parser.parse_args()

    base_url = args.url
    root_doc_name = args.root_doc_name
    output_dir = 'OUTPUT'

    os.makedirs(output_dir, exist_ok=True)

    help_system_name = 'Data/HelpSystem.xml'
    help_system_url = combine_urls(base_url, help_system_name)

    help_system_xml = get_content(help_system_url)

    toc = get_xml_attr(help_system_xml, "Toc")
    chunk = toc.replace('.js', '_Chunk0.js')

    toc_url = combine_urls(base_url, toc)
    chunk_url = combine_urls(base_url, chunk)

    toc_content = extract_define_content(get_content(toc_url))
    tree_menu_list = toc_content["tree"]["n"]
    desc_menu_list = extract_define_content(get_content(chunk_url))

    menu_structure = [fetch_menu_structure(menu, desc_menu_list, None) for menu in tree_menu_list]

    menu_structure = add_weights(menu_structure)

    generate_hugo_structure(menu_structure, base_url, output_dir, root_doc_name)


if __name__ == "__main__":
    main()

