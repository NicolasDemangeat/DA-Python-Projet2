# -*-coding:UTF-8 -*
import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv
import re
import os.path
import scraping_one_book
import pandas as pd

def find_next_page(url = ''):    
    url_all_pages_list = []
    test_url = url.replace("index", "page-1") # replace the end of the url by page-1
    reponse = requests.get(test_url)
    if reponse.ok: # if page-1 exist
        for i in range(1, 9): # try to access to all of the next pages
            url_page = url.replace("index", "page-" + str(i))
            reponse = requests.get(url_page)
            if reponse.ok:
                url_all_pages_list.append(url_page) # put the url in the list
    else:
        url_all_pages_list.append(url) # if page-1 doesn't exist, put the url in the list

    return url_all_pages_list

def scrap_one_category(url = ''): #scrap all the urls' books in the category
    links = [] # list with all urls books in the page

    urls_next_pages_list = find_next_page(url)  # ulr parameter
	
    for link in urls_next_pages_list:
        reponse = requests.get(link)
        soup = BeautifulSoup(reponse.content, 'html.parser')        
        all_title = soup.find_all('h3')
        for one_title in all_title:
            a = one_title.find('a')
            link = a['href']
            links.append(urllib.parse.urljoin("http://books.toscrape.com/catalogue/catalogue/catalogue/catalogue/", link))
    
    return links #return a list of all books' urls

def scrap_all_books(links_of_books = []): #scrap all books in the page
    df_list = []
    try:
        for link in links_of_books:
            df_list.append(scraping_one_book.scrap_one_book(link))
       
        df_all_books = pd.concat(df_list)
        return df_all_books
    except:
        print("L'URL n'est pas correct, veuillez relancer le programme.")

if __name__ == '__main__':
    the_url = scraping_one_book.set_the_url()
    links_of_books = scrap_one_category(the_url)
    category_name = scraping_one_book.download_image(links_of_books)
    scrap_all_books(links_of_books).to_csv(path_or_buf = category_name + '/' + category_name + '.csv', sep=';', index=False, encoding="utf-8-sig")
