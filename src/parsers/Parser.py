from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import ssl


def get_phones_from_page(page, get_phones_soups, get_phone_contents):
    phones_info = {}
    phones_soup = get_phones_soups(page)
    for soup in phones_soup:
        try:
            phones_info.update(get_phone_contents(soup))
        except Exception as e:
            print(e)
    return phones_info


def get_soup(page):
    soup = BeautifulSoup(open_page(page), 'html.parser')
    return soup


def open_page(page):
    # If certificate fails
    if (not os.environ.get('PYTHONHTTPSVERIFY', '')
            and getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context
    page = urlopen(page)
    page_contents = page.read().decode("utf-8")
    return page_contents
