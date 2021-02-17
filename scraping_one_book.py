# -*-coding:UTF-8 -*
import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv
import re
import os.path
import pandas as pd
import wget
from slugify import slugify

# set the url
def set_the_url():
	regex_ok = False
	while regex_ok == False: #try to set the url
		input_url = input("Veuillez saisir l'URL : ")
		pattern = '^https?://books[.]toscrape[.]com/'
		result = re.match(pattern, input_url)
		if result:		
			regex_ok = True
			return input_url
		else:
			print("L'URL n'est pas valide.")	

def scrap_one_book(url = ''):
	if __name__ == '__main__':
		the_url = set_the_url()
	else:
		the_url = url #a modifier
	
	book_info = pd.DataFrame()
	# set the response resquests
	response = requests.get(the_url)
	# if OK, scrap the page
	if response.ok:
		soup = BeautifulSoup(response.content, 'html.parser')
		product_page_url = the_url
		title = soup.h1.text
		image_url = urllib.parse.urljoin("http://books.toscrape.com/", soup.img['src']) # scrap of URL image			
		category = soup.find('ul')('li')[2].text.strip() # scrap gategory			
		all_p = soup.find_all('p') # find all paragraph			
		product_description = all_p[3].text #in all paragraph, p[3] is the description
		# find each paragraph in all paragraph
		for p in all_p:
			rewiev_p = p['class'] # find all paragraph with argument class
			if rewiev_p[0] == 'star-rating': # condition to find the paragraph with class == star rating
				review_rating = rewiev_p[1]	# select the number rating	
				break 
			
		tds = soup.find_all('td') #find all td
		universal_product_code = tds[0].text
		price_excluding_tax = tds[2].text
		price_including_tax = tds[3].text
		number_available_list = re.findall(r'\d', tds[5].text) #make a list of number
		number_available = ''.join(number_available_list) #join the number
		
		title_slug = slugify(title)
		wget.download(image_url, title_slug + '.jpg', bar=None)
		
	
	try:
		book_info = pd.DataFrame({'product_page_url': [product_page_url],
								'universal_product_code(upc)': [universal_product_code],
								'title': [title],
								'price_including_tax': [price_including_tax],
								'price_excluding_tax': [price_excluding_tax],
								'number_available': [number_available],
								'product_description': [product_description],
								'category': [category],
								'review_rating': [review_rating],
								'image_url': [image_url]})								
		
	except NameError:
		print("ERREUR : Le livre est introuvable, l'URL n'est pas valide. Relancer le programme avec une URL valide.")

	return book_info

if __name__ == '__main__':
	scrap_one_book().to_csv(path_or_buf='book_info.csv', sep=';', index=False)
