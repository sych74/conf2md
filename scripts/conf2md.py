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
    print(response)
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

def convert_to_md(html):
    soup_raw = bs4.BeautifulSoup(html, 'html.parser')
    soup = convert_atlassian_html(soup_raw)
    md_text = pypandoc.convert_text(soup, format='html', to='gfm', extra_args=['--markdown-headings=atx'])
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

def generate_md_file(data, output_dir, confluence):
    for item in data:
        path = os.path.join(output_dir, item['link'][1:])
        os.makedirs(path, exist_ok=True)
        md_filename = os.path.join(path, os.path.basename(item['link']) + '.md')
        download_attachments_from_page(item['id'], path, confluence)
        body = get_page_body(item['id'], confluence)
        md = convert_to_md(body)
        with open(md_filename, 'w') as f:
            f.write(f'''---

draft: false
title: "{item['title']}"
aliases: "/{os.path.basename(item['link'])}/"
seoindex: "index, follow"
seotitle: "{item['title']}"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "{item['title']}"
        url: "/{os.path.basename(item['link'])}/"
        weight: "{item['weight']}"
        parent: "{os.path.basename(os.path.dirname(item['link'])) if item['parentId'] else ''}"
        identifier: "{os.path.basename(item['link'])}"
---

# {item['title']}

{md}

''')

        if 'children' in item:
            generate_md_file(item['children'], output_dir, confluence)

def main():
    parser = argparse.ArgumentParser(description='Extract attributes from a webpage.')
    parser.add_argument('--url', required=True, help='URL of the confluence webpage')
    parser.add_argument('--conf_user', required=True, help='Confluence username')
    parser.add_argument('--conf_pswd', required=True, help='Confluence password')
    args = parser.parse_args()

    url = args.url
    username = args.conf_user
    password = args.conf_pswd

    attributes = get_data_attributes(url)

    for attr in attributes:
        viewport_id = attr["data-viewport-id"]
        root = attr["data-root"]
        parent = attr["data-current"]

    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
    viewport_path = "rest/scroll-viewport/1.0/tree/children"
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
    data_structure = [page for page in basic_structure.values() if page.get('parentId') is None]

    # Add weights for menu
    conf_menu_structure = add_weights(data_structure)

    output_dir = 'OUTPUT'
    os.makedirs(output_dir, exist_ok=True)
    generate_md_file(conf_menu_structure, output_dir, confluence)


if __name__ == "__main__":
    main()
