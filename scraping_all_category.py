# -*-coding:UTF-8 -*
import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv
import re
import os.path
import scraping_one_book
import scraping_one_category
import pandas as pd

def scrap_the_site():
    """
        this function return a list of all the ulr category in the site.
    """
    link = 'http://books.toscrape.com/index.html'

    req = requests.get(link)
    soup = BeautifulSoup(req.content, 'html.parser')

    links = []
    uls = soup.select('a[href^="catalogue/category/books/"]')
    for ul in uls:    
        link = ul['href']
        links.append('http://books.toscrape.com/' + link)
    return links # list of all url category

links = scrap_the_site()
for link in links:
    urls_category = scraping_one_category.scrap_one_category(link)
    category_name = scraping_one_book.download_image(urls_category)
    scraping_one_category.scrap_all_books(urls_category).to_csv(path_or_buf = category_name + '/books_info.csv', sep=';', index=False)

