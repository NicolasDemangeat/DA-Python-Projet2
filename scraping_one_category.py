# -*-coding:UTF-8 -*
import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv
import re
import os.path
import scraping_one_book

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

def scrap_all_books():
    links = scrap_one_category()
    try:
        for link in links:            
            url = urllib.parse.urljoin("http://books.toscrape.com/catalogue/catalogue/catalogue/catalogue/", link)
            scraping_one_book.scrap_one_book(url)
    except:
        print("L'URL n'est pas correct, veuillez relancer le script.")

if __name__ == '__main__':
    url_category = scraping_one_book.set_the_url()
    scrap_all_books()