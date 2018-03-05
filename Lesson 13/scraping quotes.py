#!/usr/bin/env python
# -*- coding: utf-8 -*-


from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

csv_file = open("quote_lists.csv", "w")
url = 'http://quotes.yourdictionary.com/theme/marriage/'

response = urlopen(url).read()

soup = BeautifulSoup(response)
quotes_url = 'http://quotes.yourdictionary.com/theme/marriage/'
quotes_html = urlopen(quotes_url).read()
quotes_soup = BeautifulSoup(quotes_html)
quotes = quotes_soup.findAll("p", attrs={"class": "quoteContent"})
for x in quotes:
    print x.text
    csv_file.write(x.text + "\n")

csv_file.close()