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
        Extract:
        This function search for all links of all category on the website.
        Return: list, of all URL category.
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

print("Début du programme.")
links = scrap_the_site()
bar = Bar('En cours : ', max=len(links)) #set the progress bar
for link in links:
    urls_category = scraping_one_category.scrap_one_category(link)
    category_name = scraping_one_book.download_image(urls_category)
    """
        Load:
        Push the DataFrame of one category into a csv at each lap of the loop.
    """
    scraping_one_category.scrap_all_books(urls_category).to_csv(path_or_buf = category_name + '/' + category_name + '.csv', sep=';', index=False, encoding="utf-8-sig")
    bar.next()#progress the bar
bar.finish()
print('Programme terminé sans erreur.')

