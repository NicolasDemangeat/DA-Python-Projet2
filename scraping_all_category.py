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
from progress.bar import Bar

def scrap_the_site():
    """
    Extract:\n
    This function search all links of all categories on the website.\n
    :return: a list, of all URLs categories.
    """
    link = 'http://books.toscrape.com/index.html'

    req = requests.get(link)
    soup = BeautifulSoup(req.content, 'html.parser')

    links = []
    uls = soup.select('a[href^="catalogue/category/books/"]')
    for ul in uls:    
        link = ul['href']
        links.append('http://books.toscrape.com/' + link)
    return links    #list of all url category

print("Début du programme.")
links = scrap_the_site()    #get all URLs of categories
bar = Bar('En cours : ', max=len(links))    #set the progress bar
for link in links:
    urls_category = scraping_one_category.scrap_one_category(link)
    category_name = scraping_one_book.download_image(urls_category)
    path = "Books-To-Scrape/" + category_name + '/' + category_name + '.csv'
    """
    Load:
    Push the DataFrame of one category into a csv at each lap of the loop.
    """
    scraping_one_category.scrap_all_books(urls_category).to_csv(path, sep=';', index=False, encoding="utf-8-sig")
    bar.next()  #progress the bar
bar.finish()
print('Programme terminé sans erreur.')

