Project explanation and requirements
====================================

This project is dedicated for people who is willing to buy a new mobile phone, but cannot 
find an optimal solution. There are multiple websites that show the comparison of prices
of different prices in different stores, but this is a problem for countries, where
there are no such services, and here, this project which is based on https://core.telegram.org/bots/api
gives ability to people not surf internet for hours and compare the prices by few clicks 

Requirements
------------
In order to use this project, you have to create your own bot, the process of installation is 
described here: https://core.telegram.org/bots. You have to get your own token. And run this program on server.

Supported commands:
-------------------

*/scrape* - scrapes and returns xlsx file with scraped data. Name of file is built from date when it was scraped: "(day-month-year).xlsx"

*/archive* - gives a list of scraped data for the last 31 days (one month)

*/compare* - compares two datasets, giving results about changes in the second dataset (new products, altered prices, products gone out of stock) 

*/start* - welcome message

*/help* - brief info about supported commands 

*/contact* - gives info about creator of this hyperintelligent bot


