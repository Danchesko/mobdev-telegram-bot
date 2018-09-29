from src.parsers import Parser
from src.constants import Phone


PAGE_URL = "http://mistore.kg/product-category/%D1%81%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD%D1%8B-xiaomi/"
URL_CORE = "http://mistore.kg"


def get_phones(page=PAGE_URL):
    phones_info = {}
    while True:
        phones_info.update(
            Parser.get_phones_from_page(
                page, get_phones_soups, get_phone_contents))
        page = check_page(page)
        if not page:
            break
    return phones_info


def check_page(page):
    soup = Parser.get_soup(page)
    try:
        next_page = soup.find('a', "next page-numbers")
        return next_page['href']
    except Exception:
        return None


def get_phones_soups(page):
    phones = Parser.get_soup(page).find('div','load-container').find_all(
            'div',"product-content clearfix")
    return phones


def get_phone_contents(soup):
    url = URL_CORE + soup.find('h3').a['href']
    phones_info = {url: {
           Phone.TITLE: soup.find('h3').a.text,
           Phone.PRICE: soup.find('span','price').text}}
    return phones_info
