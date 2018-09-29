from src.parsers import Parser
from src.constants import Phone

PAGE_URL = "https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/?items_per_page=%d"
ITEMS_PER_PAGE = 500


def get_phones(page=PAGE_URL % ITEMS_PER_PAGE):
    phones_info = {}
    while True:
        phones_info.update(
            Parser.get_phones_from_page(page, get_phones_soups, get_phone_info))
        page = check_page(page)
        if not page:
            break
    return phones_info


def check_page(page):
    soup = Parser.get_soup(page)
    try:
        next_page = soup.find_all('li', "bx-pax")[1]
        return next_page.parent['href']
    except Exception:
        return None


def get_phones_soups(page):
    phones = Parser.get_soup(page).find_all('a', "product-title")
    return phones


def get_phone_info(soup):
    url = soup['href']
    phone_info = {url: {Phone.TITLE: soup.text}}
    try:
        phone_info[url][Phone.PRICE] = soup.parent.next_sibling.find(
            'span', id=lambda value: value and value.startswith("sec_discounted_price")).text
    except Exception:
        phone_info[url][Phone.PRICE] = 'Предзаказ'
    return phone_info
