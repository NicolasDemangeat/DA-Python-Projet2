# -*-coding:UTF-8 -*
import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv
import re
import os.path
import scraping_one_book
import scraping_one_category

def scrap_the_site():
    link = 'http://books.toscrape.com/index.html'

    req = requests.get(link)
    soup = BeautifulSoup(req.content, 'html.parser')

    links = []
    uls = soup.select('a[href^="catalogue/category/books/"]')
    for ul in uls:    
        link = ul['href']
        links.append('http://books.toscrape.com/' + link)
    return links

links = scrap_the_site()
for link in links:
    url_category = scraping_one_category.scrap_one_category(link)
