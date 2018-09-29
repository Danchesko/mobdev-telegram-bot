import os

BOT_TOKEN = os.environ.get("TELEBOT_TOKEN")

BOT_PASS = os.environ.get("TELEBOT_PASS")

WELCOME_MESSAGE = r"""Hello, %s,
This bot will help you get and analyze the data about mobile phones from eight  different Kyrgyz trading platforms
Supported commands:
/login - pass password to use all of the bot commands
/scrape - scrapes and returns xlsx file with scraped data. Name of file is built from date when it was scraped: "(day-month-year).xlsx"
/archive - gives a list of scraped data for the last 31 days (one month)
/compare - compares two datasets, giving results about changes in the second dataset (new products, altered prices, products gone out of stock) 
/start - welcome message
/help - brief info about supported commands 
/contact - gives info about creator of this hyperintelligent bot

 How to use /compare command:
"/compare 01-09-2018 07-09-2018" (provided dates have to be in /archive in order to compare datasets)"""

HELP_MESSAGE =  r"""
Supported commands:
/login - pass password to use all of the bot commands
/scrape - scrapes and returns xlsx file with scraped data. Name of file is built from date when it was scraped: "(day-month-year).xlsx"
/archive - gives a list of scraped data for the last 31 days (one month)
/compare - compares two datasets, giving results about changes in the second dataset (new products, altered prices, products gone out of stock) 
/start - welcome message
/help - brief info about supported commands 
/contact - gives info about creator of this hyperintelligent bot

 How to use /compare command:
"/compare 01-09-2018 07-09-2018" (provided dates have to be in /archive in order to compare datasets)"""

CONTACT_INFO = "Daniiar Berdikulov. DATA SCIENTIST. VEON."

ARCHIVE_MESSAGE = "Here is the archive of the scraped data for the last month"

PARSING_MESSAGE = "Parsing %s..."

PARSE_FINISHED_MESSAGE = "Phones Parsed: %s"

INVALID_ARGUMENT_MESSAGE = 'Invalid arguments: "%s"'

UNABLE_MESSAGE = r"Unable to find given documents in /archive, please check your arguments on validity"

ERROR_MESSAGE = "An error occured when parsing the webpage, try to check if they page responds"

LOGIN_SUCCESS = "You successfully logged in. Now you can access all bot commands."

LOGIN_FAILURE = "Password is incorrect"

ACCESS_DENIED = "You don't have access to use this bot"

class Phone:
    TITLE = "Название телефона"
    SHOP = "Магазин"
    PRICE = "Цена"
    PRICE_AFTER = "Измененная цена"