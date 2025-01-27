import re
import os
import sys
import json
import requests
import argparse
import pypandoc
from urllib.parse import urljoin
from urllib.parse import urlparse
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
        if elements_with_attribute:
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

def convert_warning(soup):
    importants = soup.find_all('div', class_='warning')
    if importants:
        for important in importants:
            important_html = important.decode_contents()
            hugo_shortcode = "{{{{%note%}}}}{}{{{{%/note%}}}}".format(important_html)
            important.replace_with(BeautifulSoup(hugo_shortcode, 'html.parser'))
    return soup

def convert_mc_variable(soup):
    for span in soup.find_all('span', class_='mc-variable'):
        variable_name = next((cls for cls in span['class'] if cls != 'mc-variable' and cls != 'variable'), None)
        if variable_name:
            hugo_shortcode = '{{{{< param "{}" >}}}}'.format(variable_name)
            span.replace_with(BeautifulSoup(hugo_shortcode, 'html.parser'))
    return soup

def convert_mc_link(soup,root_doc_name):
    for link in soup.find_all('a', class_='MCXref xref'):
        if 'href' in link.attrs:
            old_href = link['href']
            clean_href = old_href.replace('.html', '')
            new_href = f"../{root_doc_name}-{clean_href}"
            link['href'] = new_href
    return soup

def convert_span_path(soup):
    for span in soup.find_all('span', class_='path'):
        span.wrap(soup.new_tag('code'))
        span.unwrap()
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
    a_tags = soup.find_all('a', class_='MCPopupThumbnailLink')
    if a_tags:
        for a_tag in a_tags:
            img_tag = a_tag.find('img', class_='MCPopupThumbnail img')
            if a_tag and img_tag:
                href = a_tag.get('href')
                href_url = combine_urls(url, href)
                href_filename = href.split('/')[-1]
                download_attachment(href_url, href_filename, output_dir)

                src = img_tag.get('src')
                src_url = combine_urls(url, src)
                src_filename = src.split('/')[-1]
                download_attachment(src_url, src_filename, output_dir)

                new_a_tag = BeautifulSoup(f'<img src="{href_filename}" alt="{href_filename}" />', 'html.parser')
                a_tag.replace_with(new_a_tag)

    return soup

def convert_mcpopup_img_old(soup, url, output_dir):
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

                new_a_tag = BeautifulSoup(f'<img src="{href_filename}" alt="{href_filename}" />', 'html.parser')
                madcap_tag.replace_with(new_a_tag)

    return soup



def download_attachment(url, name, path):
    full_name = os.path.join(path, name)
    print(url)
    print(full_name)

    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(full_name, "wb") as f:
                for bits in r.iter_content(chunk_size=8192):
                    if bits:
                        f.write(bits)
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False



def convert_procedure_heading(soup):
    headings = soup.find_all('p', class_='procedure-heading')
    if headings:
        for heading in headings:
            heading.wrap(soup.new_tag('h2'))
            heading.unwrap()
    return soup

def convert_tab_title(soup):
    titles = soup.find_all('p', class_='tab-title')
    if titles:
        for title in titles:
            title.wrap(soup.new_tag('h3'))
            title.unwrap()
    return soup


def convert_command_line_interface(soup):
    tabs = soup.find_all('div', class_='tab')
    if tabs:
        for tab in tabs:
            tab_title = tab.find('p', class_='tab-title')
            if tab_title and tab_title.text == 'Command-line interface':
                tab_title.wrap(soup.new_tag('h3'))
                tab_title.unwrap()
                dl_elements = tab.find_all('dl')
                if dl_elements:
                    for dl_element in dl_elements:
                        dt_elements = dl_element.find_all('dt')
                        dd_elements = dl_element.find_all('dd')
                        ul_element = soup.new_tag('ul')
                        for dt, dd in zip(dt_elements, dd_elements):
                            li = soup.new_tag('li')
                            b_tag = soup.new_tag('b')
                            i_tag = soup.new_tag('i')
                            i_tag.string = dt.get_text()
                            b_tag.append(i_tag)
                            li.append(b_tag)
                            li.append(f' - {dd.get_text()}')
                            ul_element.append(li)
                        dl_element.replace_with(ul_element)

    return soup


def convert_admin_panel_interface(soup):
    tabs = soup.find_all('div', class_='tab')
    if tabs:
        for tab in tabs:
            tab_title = tab.find('p', class_='tab-title')
            if tab_title and tab_title.text == 'Admin panel':
                tab_title.wrap(soup.new_tag('h3'))
                tab_title.unwrap()
    return soup

def is_relative(url):
    parsed = urlparse(url)
    return not parsed.scheme and not parsed.netloc


def convert_images(soup, url, output_dir):
    imgs = soup.find_all('img')
    if imgs:
        for img in imgs:
            src = img.get('src')
            if is_relative(src):
                src_url = combine_urls(url, src)
                src_filename = src.split('/')[-1]
                download_attachment(src_url, src_filename, output_dir)
                new_img = BeautifulSoup(f'<img src="{src_filename}" alt="{src_filename}" />', 'html.parser')
            else:
                new_img = BeautifulSoup(f'<img src="{src}" alt="{src}" />', 'html.parser')
            img.replace_with(new_img)
    return soup

def extract_and_replace_pre_tags(soup):
    pre_contents = []
    pre_counter = 0

    for i, pre_tag in enumerate(soup.find_all('pre')):
        pre_content = pre_tag.string
        if pre_content is not None:
            pre_contents.append(pre_content)
            pre_tag.replace_with(f'UNIQUE_PRE_TAG_{pre_counter}')
            pre_counter += 1

    return soup, pre_contents

def restore_pre_tags(md_text, pre_contents):
    if pre_contents:
        for i, pre_content in enumerate(pre_contents):
            pre_content = pre_content.strip()
            pre_block = f'```\n{pre_content}\n```'
            pre_placeholder = f'UNIQUE_PRE_TAG_{i}'
            placeholder_index = md_text.find(pre_placeholder)

            if placeholder_index != -1:
                before = '\n' if placeholder_index > 0 and md_text[placeholder_index-1] != '\n' else ''
                after = '\n' if placeholder_index + len(pre_placeholder) < len(md_text) and md_text[placeholder_index+len(pre_placeholder)] != '\n' else ''
                md_text = md_text.replace(pre_placeholder, f'\n{before}{pre_block}{after}')

    return md_text

def extract_and_replace_table_tags(soup):
    table_contents = []

    for i, table_tag in enumerate(soup.find_all('table')):
        table_contents.append(str(table_tag))
        table_tag.replace_with(f'UNIQUE_TABLE_TAG_{i}')

    return soup, table_contents


def restore_table_tags(md_text, table_contents):
    for i, table_content in enumerate(table_contents):
        md_text = md_text.replace(f'UNIQUE_TABLE_TAG_{i}', f'{table_content}')

    return md_text

def replace_br_tags(html):
    html = re.sub(r'<br\s*/?>', '\n', html)
    return html

def remove_div_tags(text):
    pattern = r'^(\s*</?div(?:\s+[^>]*>|>))'
    cleaned_text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.MULTILINE)
    return cleaned_text


def post_convert_shortcode(md):
    md = re.sub(r'\n*{{%note%}}', '\n\n{{%note%}}', md)
    md = re.sub(r'{{%/note%}}\n*', '{{%/note%}}\n\n', md)
    md = re.sub(r'{{%note%}}\s*\n', '{{%note%}}\n', md)
    md = re.sub(r'\n\s*{{%/note%}}', '\n{{%/note%}}', md)

    md = re.sub(r'\n*{{%tip%}}', '\n\n{{%tip%}}', md)
    md = re.sub(r'{{%/tip%}}\n*', '{{%/tip%}}\n\n', md)
    md = re.sub(r'{{%tip%}}\s*\n', '{{%tip%}}\n', md)
    md = re.sub(r'\n\s*{{%/tip%}}', '\n{{%/tip%}}', md)

    md = re.sub(r'\s*!\[\]\([^\)]*\)', lambda m: m.group(0).lstrip(), md)

    md = md.replace("\>", ">")
    md = md.replace("\<", "<")
    md = md.replace("\$", "$")
    md = md.replace("\|", "|")
    md = md.replace("\[", "[")
    md = md.replace("\]", "]")
    md = md.replace("\~", "~")
    return md

def convert_madcap_html_to_md(url, page, output_dir,root_doc_name):
    page = page.lstrip('/')
    page_url = combine_urls(url, page)
    page_html = get_page_html(page_url)
    page_html = replace_br_tags(page_html)
    soup = BeautifulSoup(page_html, 'html.parser')
    soup = get_page_main_content(soup)
    soup = convert_info(soup)
    soup = convert_important(soup)
    soup = convert_warning(soup)
    soup = convert_mc_variable(soup)
    soup = convert_span_path(soup)
    soup = convert_uicontrol(soup)

    soup = convert_dropdown(soup)
    soup = convert_mcpopup_img(soup, url, output_dir)
    soup = convert_mctextpopup(soup)
    soup = convert_mc_link(soup, root_doc_name)

    soup = convert_procedure_heading(soup)
    soup = convert_command_line_interface(soup)
    soup = convert_admin_panel_interface(soup)
    soup = convert_images(soup, url, output_dir)

    soup, pre_contents = extract_and_replace_pre_tags(soup)
    soup, table_contents = extract_and_replace_table_tags(soup)

    md_content = pypandoc.convert_text(
        soup,
        format='html',
        to='gfm',
        extra_args=['--markdown-headings=atx', '--wrap=none']
    )

    md_content = restore_table_tags(md_content, table_contents)
    md_content = restore_pre_tags(md_content, pre_contents)
    md_content = post_convert_shortcode(md_content)
    md_content = remove_div_tags(md_content)

    return md_content

def generate_hugo_structure(data, url, output_dir, root_doc_name):

    for item in data:
        path_with_prefix = add_prefix_to_directories(item['link'][1:], root_doc_name)
        path = os.path.join(output_dir, path_with_prefix)

        if 'children' in item:
            path_with_prefix = add_prefix_to_directories(os.path.basename(item['link']), root_doc_name)
            path = os.path.join(path, path_with_prefix)
        os.makedirs(path, exist_ok=True)

        md_content = convert_madcap_html_to_md(url, item['page_url'], path, root_doc_name)
        identifier = root_doc_name if root_doc_name == os.path.basename(item['link']) else f"{root_doc_name}-{os.path.basename(item['link'])}"
        parent = root_doc_name if root_doc_name == os.path.basename(os.path.dirname(item['link'])) else f"{root_doc_name}-{os.path.basename(os.path.dirname(item['link']))}"
        parent_id = parent if item['parentId'] else root_doc_name
        title = item['title']
        weight = item['weight']

        generate_index_md(path, title, identifier, parent_id, md_content, weight)

        if 'children' in item:
            generate_hugo_structure(item['children'], url, output_dir, root_doc_name)


def generate_index_md(path, title, identifier, parent_id, md_content, weight, pdf=None):
    md_filename = os.path.join(path, 'index.md')
    os.makedirs(path, exist_ok=True)

    md_content_header = f'''---
draft: false
title: "{title}"
aliases: "/{identifier}/"
seoindex: "index, follow"
seotitle: "{title}"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "{title}"
        url: "/{identifier}/"
        weight: "{weight}"
        parent: "{parent_id}"
        identifier: "{identifier}"
'''

    if pdf:
        md_content_header += f'''        params:
            pdf: "{pdf}"
'''

    md_content_header += f'''---

{md_content}

'''

    with open(md_filename, 'w') as f:
        f.write(md_content_header)

def generate_main_index_md(url, output_dir, root_doc_name):
    path = os.path.join(output_dir, root_doc_name)
    os.makedirs(path, exist_ok=True)
    title = root_doc_name
    identifier = root_doc_name
    parent_id = ""
    md_content = ""
    weight = 1
    pdf = get_pdf_from_url(url)
    if download_attachment(pdf['pdf_url'], pdf['pdf_filename'], path):
        generate_index_md(path, title, identifier, parent_id, md_content, weight, pdf['pdf_filename'])
    else:
        generate_index_md(path, title, identifier, parent_id, md_content, weight)


def get_pdf_from_url(url):
    parts = url.rstrip('/').rsplit('/', 1)
    base_url = parts[0]
    segment = parts[1]
    pdf_url = f"{base_url}/pdf/{segment}.pdf"
    pdf_filename = f"{segment}.pdf"
    return {'pdf_url': pdf_url, 'pdf_filename': pdf_filename}


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

    generate_main_index_md(base_url, output_dir, root_doc_name)

    generate_hugo_structure(menu_structure, base_url, output_dir, root_doc_name)


if __name__ == "__main__":
    main()

