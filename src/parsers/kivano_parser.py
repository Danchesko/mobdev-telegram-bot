from src.parsers import Parser
from src.constants import Phone

PAGE_URL = 'https://www.kivano.kg/mobilnye-telefony?page=%d'
URL_CORE = 'https://www.kivano.kg'


def get_phones(page=PAGE_URL):
    phones_info = {}
    for i in range(1, int(check_last_page(page)) + 1):
        phones_info.update(
            Parser.get_phones_from_page(
                page % i, get_phones_soups, get_phone_contents))
    return phones_info


def check_last_page(page):
    soup = Parser.get_soup(page)
    last_page = soup.find('li', "last")
    return last_page.a.text


def get_phones_soups(page):
    phones = Parser.get_soup(page).find_all('div', "pull-right rel")
    return phones


def get_phone_contents(soup):
    phones_info = {}
    info = soup.find_all("strong")
    url = URL_CORE + info[0].a['href']
    phones_info[url] = {
            Phone.TITLE: info[0].a.text,
            Phone.PRICE: info[1].text}
    return phones_info
