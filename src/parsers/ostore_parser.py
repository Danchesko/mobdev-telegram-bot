from src.parsers import Parser
from src.constants import Phone
PAGE_URL = 'https://ostore.kg/phones/?SORT_TO=%d'
URL_CORE = 'https://ostore.kg'
ITEMS_PER_PAGE = 100


def get_phones(page=PAGE_URL % ITEMS_PER_PAGE):
    phones_info = {}
    while True:
        phones_info.update(
            Parser.get_phones_from_page(page, get_phones_soups, get_phone_info))
        page = check_page(page)
        if not page:
            break
        page = URL_CORE + page
    return phones_info


def check_page(page):
    soup = Parser.get_soup(page)
    try:
        next_page = soup.find('li', "bx-pag-next")
        return next_page.a['href']
    except Exception:
        return None


def get_phones_soups(page):
    phones = Parser.get_soup(page).find(
        'div', 'items productList').find_all('a', "name")
    return phones


def get_phone_info(soup):
    url = URL_CORE + soup['href']
    phone_info = {url: {
            Phone.TITLE: soup.text,
            Phone.PRICE: soup.find_next_sibling().contents[0].strip()}}
    return phone_info
