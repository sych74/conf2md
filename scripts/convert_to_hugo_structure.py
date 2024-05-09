import os
import re
import bs4
import json
import requests
from atlassian import Confluence
from markdownify import markdownify as md

url = ''
username = ''
password = ''

confluence = Confluence(
    url=url,
    username=username,
    password=password)


def get_page_body(page_id):
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

            # construct new, actually valid HTML tag
#            srcurl = os.path.join("test", url)
#            imgtag = soup.new_tag("img", attrs={"src": srcurl, "alt": srcurl})
            imgtag = soup.new_tag("img", attrs={"src": url, "alt": url})
            # insert a linebreak after the original "ac:image" tag, then replace with an actual img tag
            image.insert_after(soup.new_tag("br"))
            image.replace_with(imgtag)
        return soup

def remove_empty_lines(md_text):
    return re.sub(r'\n{2,}', '\n', md_text)


def convert_to_md(html):
    soup_raw = bs4.BeautifulSoup(html, 'html.parser')
    soup = convert_atlassian_html(soup_raw)
    md_text = md(str(soup), heading_style="ATX", code_style="fenced", bullet_style="dash")
    md_text = remove_empty_lines(md_text)
    return md_text


def download_attachments_from_page(page_id, path):
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



def generate_md_file(data, output_dir):
    for item in data:
        path = os.path.join(output_dir, item['link'][1:])
        os.makedirs(path, exist_ok=True)
        md_filename = os.path.join(path, os.path.basename(item['link']) + '.md')
        download_attachments_from_page(item['id'], path)
        body = get_page_body(item['id'])
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
        weight: 10
        parent: "{os.path.basename(os.path.dirname(item['link'])) if item['parentId'] else 'vhs9ag'}"
        identifier: "{os.path.basename(item['link'])}"
---

# {item['title']}

{md}

''')

        if 'children' in item:
            generate_md_file(item['children'], output_dir)

def main(json_data):
    output_dir = 'OUTPUT'
    os.makedirs(output_dir, exist_ok=True)
    generate_md_file(json_data, output_dir)

if __name__ == "__main__":
    with open('menu_structure.json', 'r') as f:
        json_data = json.load(f)

    main(json_data)

