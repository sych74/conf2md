import os
import re
import bs4
import sys
import json
import requests
import argparse
import pypandoc
import urllib.parse
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from atlassian import Confluence

def add_weights(data):
    def set_weight(item, weight):
        item['weight'] = weight
        if 'children' in item:
            for i, child in enumerate(item['children']):
                set_weight(child, i + 1)

    for i, item in enumerate(data):
        set_weight(item, i + 1)

    return data

def get_data_attributes(url):
    response = requests.get(url)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    ul_elements = soup.find_all('ul')
    data_attributes = []

    for ul in ul_elements:
        data_viewport_id = ul.get('data-viewport-id')
        data_root = ul.get('data-root')
        data_current = ul.get('data-current')

        if data_viewport_id and data_root and data_current:
            data_attributes.append({
                'data-viewport-id': data_viewport_id,
                'data-root': data_root,
                'data-current': data_current
            })

    return data_attributes

def fetch_menu_structure(base_url, viewport_id, root, parent, parentId=None, current_structure=None, fetched_urls=None):
    """
    Fetch the basic menu structure with child IDs, ensuring children are linked only to their respective parents,
    with URL encoding to handle special characters.
    """
    if current_structure is None:
        current_structure = {}
    if fetched_urls is None:
        fetched_urls = set()

    # URL encode the parameters
    encoded_root = urllib.parse.quote(root)
    encoded_parent = urllib.parse.quote(parent)

    # Construct the query URL
    url = f"{base_url}?viewportId={viewport_id}&root={encoded_root}&parent={encoded_parent}"
    if url in fetched_urls:
        print(f"URL already fetched, skipping: {url}")
        return current_structure
    fetched_urls.add(url)

    print(f"Fetching URL: {url}")
    response = requests.get(url)
    response_data = response.json()

    for page in response_data:
        page_id = page['id']
        if page_id not in current_structure:
            current_structure[page_id] = {
                'type': page['type'],
                'id': page['id'],
                'title': page['title'],
                'link': page['link'],
                'labels': page.get('labels', []),
                'children_ids': [],
                'parentId': parentId  # Store the parentId for later validation in child population
            }
            print(f"Processing page: {page['title']} with ID: {page['id']}")

        link_current = page['link']
        if link_current:
            encoded_link_current = urllib.parse.quote(link_current)
            if f"{base_url}?viewportId={viewport_id}&root={root}&parent={encoded_link_current}" not in fetched_urls:
                fetch_menu_structure(base_url, viewport_id, root, link_current, page_id, current_structure, fetched_urls)

    return current_structure

def populate_children(structure):
    """
    Populate children from IDs using a non-recursive approach, validating against parentId.
    Remove 'children_ids' after processing to clean up structure.
    """
    for page_id, page in structure.items():
        if 'parentId' in page and page['parentId'] is not None:
            parent_id = page['parentId']
            if parent_id in structure:
                structure[parent_id].setdefault('children', []).append(page)
                print(parent_id)
        # Clean up the 'children_ids' key
        if 'children_ids' in page:
            del page['children_ids']

def get_page_body(page_id, confluence):
    page = confluence.get_page_by_id(page_id, expand="body.storage")
    page_title = page["title"]
    page_id = page["id"]
    body = page["body"]["storage"]["value"]
    return body

def convert_atlassian_html(soup):
        for image in soup.find_all("ac:image"):
            url = None
            for child in image.children:
                url = child.get("ri:filename", None)
                break

            if url is None:
                continue

            imgtag = soup.new_tag("img", attrs={"src": url, "alt": url})
            image.insert_after(soup.new_tag("br"))
            image.replace_with(imgtag)
        return soup

def remove_empty_lines(md_text):
    return re.sub(r'\n{2,}', '\n', md_text)


def convert_macro_note(soup):
    note_macros = soup.find_all('ac:structured-macro', {'ac:name': 'note'})
    if note_macros:
        for note_macro in note_macros:
            rich_text_body = note_macro.find('ac:rich-text-body')
            if rich_text_body:
                note_html = rich_text_body.decode_contents()
                hugo_shortcode = "{{{{%note%}}}}{}{{{{%/note%}}}}".format(note_html)
                note_macro.replace_with(BeautifulSoup(hugo_shortcode, 'html.parser'))
    return soup

def convert_macro_info(soup):
    info_macros = soup.find_all('ac:structured-macro', {'ac:name': 'info'})
    if info_macros:
        for info_macro in info_macros:
            rich_text_body = info_macro.find('ac:rich-text-body')
            if rich_text_body:
                info_html = rich_text_body.decode_contents()
                hugo_shortcode = "{{{{%tip%}}}}{}{{{{%/tip%}}}}".format(info_html)
                info_macro.replace_with(BeautifulSoup(hugo_shortcode, 'html.parser'))
    return soup

def convert_macro_warning(soup):
    info_macros = soup.find_all('ac:structured-macro', {'ac:name': 'warning'})
    if info_macros:
        for info_macro in info_macros:
            rich_text_body = info_macro.find('ac:rich-text-body')
            if rich_text_body:
                info_html = rich_text_body.decode_contents()
                hugo_shortcode = "{{{{%tip%}}}}{}{{{{%/tip%}}}}".format(info_html)
                info_macro.replace_with(BeautifulSoup(hugo_shortcode, 'html.parser'))
    return soup

def convert_macro_code(soup):
    code_macros = soup.find_all('ac:structured-macro', {'ac:name': 'code'})
    if code_macros:
        for code_macro in code_macros:
            plain_text_body = code_macro.find('ac:plain-text-body')
            if plain_text_body:
                code_html = plain_text_body.decode_contents()
                hugo_shortcode = "{{{{structured-macro-code-start}}}}{}{{{{structured-macro-code-end}}}}".format(code_html)
                code_macro.replace_with(BeautifulSoup(hugo_shortcode, 'html.parser'))
    return soup

def post_convert_macro_code(md):
    md = re.sub(r'\s*{{structured-macro-code-start}}', '{{structured-macro-code-start}}', md)
    md = md.replace("{{structured-macro-code-start}}", "\n```\n")
    md = md.replace("{{structured-macro-code-end}}", "\n```\n")
    return md

def post_convert_shortcode(md):
    md = re.sub(r'(?<!\n){{%note%}}', '\n{{%note%}}\n', md)
    md = re.sub(r'{{%/note%}}(?!\n)', '\n{{%/note%}}\n', md)
    md = re.sub(r'(?<!\n){{%tip%}}', '\n{{%tip%}}\n', md)
    md = re.sub(r'{{%/tip%}}(?!\n)', '\n{{%/tip%}}\n', md)

#    md = md.replace("{{%note%}}", "\n{{%note%}}\n")
#    md = md.replace("{{%/note%}}", "\n{{%/note%}}\n")
#    md = md.replace("{{%tip%}}", "\n{{%tip%}}\n")
#    md = md.replace("{{%/tip%}}", "\n{{%/tip%}}\n")
    md = md.replace("{{pre}}", "\n")
    md = md.replace("\>", ">")
    md = md.replace("\<", "<")
    md = md.replace("\$", "$")
    md = md.replace("\|", "|")
    md = md.replace("\[", "[")
    md = md.replace("\]", "]")
    md = md.replace("\~", "~")

    return md

def remove_span_tags(soup):
    spans = soup.find_all('span')
    for span in spans:
        span.unwrap()

    return soup

def remove_p_tags(soup):
    spans = soup.find_all('p')
    for span in spans:
        span.unwrap()

    return soup

def remove_span_from_code(soup):
    code_elements = soup.find_all('code')
    for code in code_elements:
        spans = code.find_all('span')
        for span in spans:
            span.unwrap()
    return soup

def remove_macro_anchor(soup):
    anchor_macros = soup.find_all('ac:structured-macro', {'ac:name': 'anchor'})
    if anchor_macros:
        for anchor_macro in anchor_macros:
            anchor_macro.extract()
    return soup

def fix_strong_tag(soup):
    strong_tags = soup.find_all('strong')
    for tag in strong_tags:
        if tag.string:
            tag.string.replace_with(tag.string.strip())
        if tag.previous_sibling is None or (tag.previous_sibling.string and tag.previous_sibling.string[-1] != ' '):
            tag.insert_before(' ')
        if tag.next_sibling is None or (tag.next_sibling.string and tag.next_sibling.string[0] != ' '):
            tag.insert_after(' ')
    return soup

def fix_em_tag(soup):
    em_tags = soup.find_all('em')
    for tag in em_tags:
        if tag.string:
            tag.string.replace_with(tag.string.strip())
        if tag.previous_sibling is None or (tag.previous_sibling.string and tag.previous_sibling.string[-1] != ' '):
            tag.insert_before(' ')
        if tag.next_sibling is None or (tag.next_sibling.string and tag.next_sibling.string[0] != ' '):
            tag.insert_after(' ')
    return soup


def convert_macro_ui_steps(soup):
    code_macros = soup.find_all('ac:structured-macro', {'ac:name': 'ui-steps'})
    if code_macros:
        for code_macro in code_macros:
            plain_text_body = code_macro.find('ac:plain-text-body')
            if plain_text_body:
                code_html = plain_text_body.decode_contents()
                hugo_shortcode = "<code>{}</code>".format(code_html)
                code_macro.replace_with(BeautifulSoup(hugo_shortcode, 'html.parser'))
    return soup

def fix_ol_tag(soup):
    ol_tags = soup.find_all('ol')
    for tag in ol_tags:
        print("------", tag)
    return soup

def pre_convert(html):
    html = html.replace("\n", "{{pre}}")
    return html

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

#    pattern = r'\s*</?div(?:\s+[^>]*>|>)'
#    cleaned_text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    return cleaned_text

def remove_hr_tags(soup):
    hrs = soup.find_all('hr')
    for hr in hrs:
        hr.decompose()
    return soup

def remove_macro_with_tf_popover(soup):
    sections = soup.find_all('ac:structured-macro')
    for section in sections:
        cdata_elements = section.find_all('ac:plain-text-body')
        for cdata in cdata_elements:
            cdata_content = BeautifulSoup(cdata.string, 'html.parser') if cdata.string else None
            if cdata_content and cdata_content.find('div', {'data-tf-popover': True}):
                section.decompose()
                break
    return soup

def remove_section_with_tf_popover(soup):
    sections = soup.find_all('ac:layout-section')
    for section in sections:
        cdata_elements = section.find_all('ac:plain-text-body')
        for cdata in cdata_elements:
            cdata_content = BeautifulSoup(cdata.string, 'html.parser') if cdata.string else None
            if cdata_content and cdata_content.find('div', {'data-tf-popover': True}):
                section.decompose()
                break
    return soup

def extract_and_replace_macro_code(soup):
    macro_code_contents = []
    macro_code_counter = 0

    for i, macro_code_tag in enumerate(soup.find_all('ac:structured-macro', {'ac:name': 'code'})):
        macro_code_content = macro_code_tag.find('ac:plain-text-body')
        if macro_code_content is not None:
            macro_code_content = macro_code_content.decode_contents()
            macro_code_contents.append(macro_code_content)
            macro_code_tag.replace_with(f'UNIQUE_MACRO_CODE_TAG_{macro_code_counter}')
            macro_code_counter += 1

    return soup, macro_code_contents

def restore_macro_code_tags(md_text, macro_code_contents):
    if macro_code_contents:
        for i, macro_code_content in enumerate(macro_code_contents):
            macro_code_content = macro_code_content.strip()
            pre_block = f'```\n{macro_code_content}\n```'
            pre_placeholder = f'UNIQUE_MACRO_CODE_TAG_{i}'
            placeholder_index = md_text.find(pre_placeholder)

            if placeholder_index != -1:
                before = '\n' if placeholder_index > 0 and md_text[placeholder_index-1] != '\n' else ''
                after = '\n' if placeholder_index + len(pre_placeholder) < len(md_text) and md_text[placeholder_index+len(pre_placeholder)] != '\n' else ''
                md_text = md_text.replace(pre_placeholder, f'\n{before}{pre_block}{after}')

    return md_text

def extract_and_replace_pre_tags(soup):
    pre_contents = []
    pre_counter = 0

    for i, pre_tag in enumerate(soup.find_all('pre')):
        pre_content = pre_tag.decode_contents()
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

def remove_macro_emoticon(soup):
    emoticons = soup.find_all('ac:emoticon')
    for emoticon in emoticons:
        emoticon.decompose()
    return soup

def remove_cdata(md_text):
    return md_text.replace("<![CDATA[", "").replace("]]>", "")

def merge_pre_tags_with_newlines(html):
    return re.sub(r'(</pre>\s*<pre>)+', '\n', html)

def convert_conf_html_to_md(html):
#    html = pre_convert(html)
    html = merge_pre_tags_with_newlines(html)
    html = replace_br_tags(html)
    html = remove_cdata(html)

    soup = bs4.BeautifulSoup(html, 'html5lib')
    #soup = fix_ol_tag(soup)
    soup = fix_em_tag(soup)
    soup = fix_strong_tag(soup)
    soup = remove_hr_tags(soup)
    soup = remove_macro_emoticon(soup)
#    soup = remove_p_tags(soup)
    soup = remove_span_from_code(soup)
    soup = remove_span_tags(soup)
    soup = remove_section_with_tf_popover(soup)
    soup = remove_macro_with_tf_popover(soup)
    soup = remove_macro_anchor(soup)
    soup = convert_macro_ui_steps(soup)
    soup = convert_macro_note(soup)
#    soup = convert_macro_code(soup)
    soup = convert_macro_info(soup)
    soup = convert_macro_warning(soup)
    soup = convert_atlassian_html(soup)
    soup, macro_code_contents = extract_and_replace_macro_code(soup)
    soup, pre_contents = extract_and_replace_pre_tags(soup)
    soup, table_contents = extract_and_replace_table_tags(soup)
    md_text = pypandoc.convert_text(soup, format='html', to='gfm', extra_args=['--markdown-headings=atx', '--wrap=none'])
    md_text = restore_table_tags(md_text, table_contents)
    md_text = restore_pre_tags(md_text, pre_contents)
    md_text = restore_macro_code_tags(md_text, macro_code_contents)
#    md_text = post_convert_macro_code(md_text)
    md_text = post_convert_shortcode(md_text)
#    md_text = remove_cdata(md_text)
    md_text = remove_div_tags(md_text)
    return md_text

def download_attachments_from_page(page_id, path, confluence):
    attachments_container = confluence.get_attachments_from_content(page_id=page_id, start=0, limit=500)
    attachments = attachments_container['results']
    for attachment in attachments:
        fname = attachment['title']
        full_fname = os.path.join(path, fname)
        download_link = confluence.url + attachment['_links']['download']
        print(download_link)
        r = requests.get(download_link, auth=(confluence.username, confluence.password))
        if r.status_code == 200:
            with open(full_fname, "wb") as f:
                for bits in r.iter_content():
                    f.write(bits)

def add_prefix_to_directories(path, prefix):
    parts = path.strip(os.sep).split(os.sep)
    new_parts = [f"{prefix}-{part}" for part in parts]
    new_path = os.sep.join(new_parts)
    return new_path


def generate_hugo_structure(data, url, output_dir, confluence, root_doc_name):

    for item in data:
        path_with_prefix = add_prefix_to_directories(item['link'][1:], root_doc_name)
        path = os.path.join(output_dir, path_with_prefix)

        if 'children' in item:
            path_with_prefix = add_prefix_to_directories(os.path.basename(item['link']), root_doc_name)
            path = os.path.join(path, path_with_prefix)
        os.makedirs(path, exist_ok=True)

#        download_attachments_from_page(item['id'], path, confluence)
        body = get_page_body(item['id'], confluence)
#        body = get_page_body(151159230, confluence)

        md_content = convert_conf_html_to_md(body)

        identifier = root_doc_name if root_doc_name == os.path.basename(item['link']) else f"{root_doc_name}-{os.path.basename(item['link'])}"
        parent = root_doc_name if root_doc_name == os.path.basename(os.path.dirname(item['link'])) else f"{root_doc_name}-{os.path.basename(os.path.dirname(item['link']))}"
        parent_id = parent if item['parentId'] else root_doc_name
        title = item['title']
        weight = item['weight']

        generate_index_md(path, title, identifier, parent_id, md_content, weight)

        if 'children' in item:
            generate_hugo_structure(item['children'], url, output_dir, confluence, root_doc_name)



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

# {title}

{md_content}

'''

    with open(md_filename, 'w') as f:
        f.write(md_content_header)


def generate_main_index_md(output_dir, root_doc_name):
    path = os.path.join(output_dir, root_doc_name)
    os.makedirs(path, exist_ok=True)
    title = root_doc_name
    identifier = root_doc_name
    parent_id = ""
    md_content = ""
    weight = 1
    generate_index_md(path, title, identifier, parent_id, md_content, weight)

def main():
    parser = argparse.ArgumentParser(description='Extract attributes from a webpage.')
    parser.add_argument('--url', required=True, help='URL of the confluence webpage')
    parser.add_argument('--conf_user', required=True, help='Confluence username')
    parser.add_argument('--conf_pswd', required=True, help='Confluence password')
    parser.add_argument('--root_doc_name', required=True, help='Hugo root doc name')
    args = parser.parse_args()

    url = args.url
    username = args.conf_user
    password = args.conf_pswd
    root_doc_name = args.root_doc_name


    output_dir = 'OUTPUT'
    os.makedirs(output_dir, exist_ok=True)

    attributes = get_data_attributes(url)

    for attr in attributes:
        viewport_id = attr["data-viewport-id"]
        root = attr["data-root"]
        parent = attr["data-current"]

    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    viewport_path = "/rest/scroll-viewport/1.0/tree/children"
    viewport_url = urljoin(base_url, viewport_path)

    confluence = Confluence(
        url=base_url,
        username=username,
        password=password)

    # Fetch the complete basic structure
    basic_structure = fetch_menu_structure(viewport_url, viewport_id, root, parent)

    # Populate the full tree structure ensuring correct parent-child relationships
    populate_children(basic_structure)

    # Filter and serialize the populated structure to include only top-level pages (where parentId is null)
    menu_structure = [page for page in basic_structure.values() if page.get('parentId') is None]

    # Add weights for menu
    menu_structure = add_weights(menu_structure)

    generate_main_index_md(output_dir, root_doc_name)

    generate_hugo_structure(menu_structure, url, output_dir, confluence, root_doc_name)


if __name__ == "__main__":
    main()
