import requests
import json
import urllib.parse
import sys

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
    
    print(response_data)

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
        # Clean up the 'children_ids' key
        if 'children_ids' in page:
            del page['children_ids']

# Parse command line arguments or use default values
args = sys.argv[1:]
viewport_id = args[0] if len(args) > 0 else "45A8E00F018D55DFA3EE66266AAE79C2"
root = args[1] if len(args) > 1 else "/vhsinstallationguide/7.1beta"
parent = args[2] if len(args) > 2 else "/vhsinstallationguide/7.1beta"

# Base API parameters
BASE_URL = "https://docs.onapp.com/rest/scroll-viewport/1.0/tree/children"

# Fetch the complete basic structure
basic_structure = fetch_menu_structure(BASE_URL, viewport_id, root, parent)

# Populate the full tree structure ensuring correct parent-child relationships
populate_children(basic_structure)

# Filter and serialize the populated structure to include only top-level pages (where parentId is null)
output_data = [page for page in basic_structure.values() if page.get('parentId') is None]

with open('menu_structure.json', 'w') as file:
    json.dump(output_data, file, indent=4)

print("Data has been saved to 'menu_structure.json'.")
