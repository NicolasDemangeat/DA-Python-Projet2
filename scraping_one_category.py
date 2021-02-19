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
    """
    Extract: \n
    :Param: string, an URL category. \n
    This function test if the url parameter have more than one page.\n
    If more than one page, find all the pages and put in a list.\n
    If just one page, put the URL in the list.\n
    :return: a list of all URLs pages.
    """
    url_all_pages_list = []
    test_url = url.replace("index", "page-1")    #replace the end of the url by page-1
    reponse = requests.get(test_url)
    if reponse.ok:    #if page-1 exist
        for i in range(1, 9):   #try to access to all of the next pages
            url_page = url.replace("index", "page-" + str(i))
            reponse = requests.get(url_page)
            if reponse.ok:
                url_all_pages_list.append(url_page)    #put the url in the list
    else:
        url_all_pages_list.append(url)  #if page-1 doesn't exist, put the url parameter in the list

    return url_all_pages_list 

def scrap_one_category(url = ''):
    """
    Extract:\n
    :param: string, an URL category.\n
    This function call find_next_page to find all pages.\n
    Then extract all books URLs in all pages and put them in a list.\n
    :return: a list with all URLs books in the pages.
    """
    links = [] 
    urls_next_pages_list = find_next_page(url)  #ulr parameter
    for link in urls_next_pages_list:
        reponse = requests.get(link)
        soup = BeautifulSoup(reponse.content, 'html.parser')
        all_title = soup.find_all('h3')
        for one_title in all_title:
            a = one_title.find('a')
            link = a['href']
            links.append(urllib.parse.urljoin("http://books.toscrape.com/catalogue/catalogue/catalogue/catalogue/", link))

    return links    #list with all URLs books in the pages

def scrap_all_books(links_of_books = []):
    """
    This function is in two part:\n
    Extract:\n
    :param links_of_books: list of all the URLs books.\n
    The first part use scrap_one_book function from scraping_one_book.py,
    and extract all infos of all books in the category.\n
    Remember, the return of scrap_one_book is a DataFrame.\n
    Then append them into a list.\n
    The second part use Pandas to concat all DataFrames in the list.\n
    :return: a DataFrame of all books in a category.     
    """
    df_list = []
    try:
        for link in links_of_books:
            df_list.append(scraping_one_book.scrap_one_book(link))  #put all DataFrame in a list
        """    
        Transform:
        """ 
        df_all_books = pd.concat(df_list)
        return df_all_books
    except:
        print("L'URL n'est pas correct, veuillez relancer le programme.")

if __name__ == '__main__':
    the_url = scraping_one_book.set_the_url()
    links_of_books = scrap_one_category(the_url)
    category_name = scraping_one_book.download_image(links_of_books)
    """
    Load:
    Push the DataFrame into a csv file.
    """
    scrap_all_books(links_of_books).to_csv(path_or_buf = category_name + '/' + category_name + '.csv', sep=';', index=False, encoding="utf-8-sig")
