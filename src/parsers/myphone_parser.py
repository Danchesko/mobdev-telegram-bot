from src.parsers import Parser
from src.constants import Phone
PAGE_URL = "https://www.myphone.kg/catalog/cell?ajax=true&ord=price&di=down&all=true"
URL_CORE ="https://www.myphone.kg"


def get_phones(page=PAGE_URL):
    phones_info = {}
    phones_soup = get_phones_soups(page)
    for i in phones_soup:
        url = URL_CORE + i.a['href']
        phones_info[url] = get_phone_info(i)
    return phones_info


def get_phones_soups(page):
    phones = Parser.get_soup(page).find_all('div', "oneItem")
    return phones


def get_phone_info(info):
    phone_info = {
            Phone.TITLE: info.find('div', 'title').a.text,
            Phone.PRICE: info.find('div', 'price').a.text}
    return phone_info
