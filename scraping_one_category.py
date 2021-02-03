# -*-coding:UTF-8 -*
import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv
import re
import os.path
import scraping_one_book

url_category = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'

def scrap_one_category():
    response = requests.get(url_category)
	# if OK, scrap the page
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        all_title = soup.find_all('h3')
        for one_title in all_title:
            a = one_title.find('a')
            link = a['href']
            links.append(link)
        return links

links = scrap_one_category()
for link in links:
    url = urllib.parse.urljoin("http://books.toscrape.com/catalogue/", link[9:])
    scraping_one_book.scrap_one_book(url)




