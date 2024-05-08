import json
import os

def generate_md_file(data, output_dir):
    for item in data:
        path = os.path.join(output_dir, item['link'][1:])
        os.makedirs(path, exist_ok=True)
        md_filename = os.path.join(path, os.path.basename(item['link']) + '.md')
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
        parent: "{os.path.basename(os.path.dirname(item['link'])) if item['parentId'] else 'vhsinstallationguide'}"
        identifier: "{os.path.basename(item['link'])}"
---''')

        if 'children' in item:
            generate_md_file(item['children'], output_dir)

def main(json_data):
    output_dir = 'OUTPUT'
    os.makedirs(output_dir, exist_ok=True)
    generate_md_file(json_data, output_dir)

if __name__ == "__main__":
    with open('menu.json', 'r') as f:
        json_data = json.load(f)

    main(json_data)

