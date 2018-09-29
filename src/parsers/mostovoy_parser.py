from src.parsers import Parser
from src.constants import Phone

PAGE_URL = "http://mostovoy.kg/category/telefony"
URL_CORE = 'http://mostovoy.kg'


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
        next_page = soup.find('li', "next")
        return URL_CORE+next_page.a['href']
    except Exception:
        return None
    

def get_phones_soups(page):
    phones = Parser.get_soup(page).find_all('div', "item-disc")
    return phones


def get_phone_info(soup):
    url = URL_CORE + soup.a["href"]
    phone_info = {url: {
            Phone.TITLE: soup.a.text,
            Phone.PRICE: soup.div.text}}
    return phone_info
