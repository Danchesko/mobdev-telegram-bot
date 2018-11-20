Tutorial
========
This is a tutorial for use of the commands in the Telegram bot.

Bot Father
----------
Use BotFather to create a bot 
https://telegram.me/BotFather

Commands examples
-----------------
*/scrape* - scrapes and returns xlsx file with scraped data. Name of file is built from date when it was scraped: "(day-month-year).xlsx"::

    /scrape

*/archive* - gives a list of scraped data for the last 31 days (one month)::

    /archive

*/compare* - compares two datasets, giving results about changes in the second dataset (new products, altered prices, products gone out of stock)
The results are give in xlsx format ::

    /compare 01-01-2018 05-01-2018

*/start* - welcome message::

    /start

*/help* - brief info about supported commands ::

    /help

*/contact* - gives info about creator of this hyperintelligent bot::

    /contact
