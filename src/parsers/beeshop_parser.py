from src.parsers import Parser
from src.constants import Phone

PAGE_URL = "https://beeshop.kg/bishkek/c/smartphones"
URL_CORE = 'https://beeshop.kg'


def get_phones(page=PAGE_URL):
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
        next_page = soup.find('a', "pagination__item_next")
        return URL_CORE+next_page['href']
    except Exception:
        return None
    

def get_phones_soups(page):
    phones = Parser.get_soup(page).find_all('a', "card-text")
    return phones


def get_phone_info(soup):
    url = URL_CORE + soup["href"]
    phone_info = {url: {
            Phone.TITLE: soup.text,
            Phone.PRICE: soup.parent.find_next_sibling().find("span", "product__price").text}}
    return phone_info
