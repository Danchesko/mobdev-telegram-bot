from src.parsers import Parser
from src.constants import Phone
PAGE_URL = "https://softech.kg/pricelist"


def get_phones(page=PAGE_URL):
    phones_info = {}
    phones_soup = get_phones_soups(page)
    for i in phones_soup:
        phones_info[i.td.text] = get_phone_info(i)
    return phones_info


def get_phones_soups(page):
    phones = Parser.get_soup(page).find_all('tr', attrs={"height": 20})[5:]
    return phones


def get_phone_info(info):
    phone_info = {Phone.TITLE: info.td.text,
                  Phone.PRICE: info.td.find_next_sibling().text}
    return phone_info
