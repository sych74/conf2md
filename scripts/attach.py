from atlassian import Confluence
import requests


url = 'https://test.com'
username = 'test'
password = 'test'

# Инициализируем объект Confluence
confluence = Confluence(
    url=url,
    username=username,
    password=password)


def download_attachments_from_page(page_id):
    attachments_container = confluence.get_attachments_from_content(page_id=page_id, start=0, limit=500)
    attachments = attachments_container['results']
    for attachment in attachments:
        fname = attachment['title']
        download_link = confluence.url + attachment['_links']['download']
        print(download_link)
        r = requests.get(download_link, auth=(confluence.username, confluence.password))
        if r.status_code == 200:
            with open(fname, "wb") as f:
                for bits in r.iter_content():
                    f.write(bits)
test = download_attachments_from_page (194478151)
