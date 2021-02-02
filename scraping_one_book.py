# -*-coding:UTF-8 -*
import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv
import re

def save_info_in_csv(book_info):
	with open(f'book.csv', 'w', encoding = 'utf-8-sig') as csvfile:
		writer = csv.DictWriter(csvfile, book_info, dialect='excel', delimiter = ';')
		writer.writeheader()
		writer.writerow(book_info)

# set the url
def set_the_url():
	regex_ok = False
	while regex_ok == False: #try to set the url
		input_url = input("Veuillez saisir l'URL du livre : ")
		pattern = '^http://books[.]toscrape[.]com/catalogue/.+/index.html'
		result = re.match(pattern, input_url)
		if result:		
			the_url = input_url
			regex_ok = True
		else:
			print("L'URL n'est pas valide, elle doit être de la forme http://books.toscrape.com/catalogue/{nom_du_livre}/index.html")
	return the_url

def scrap_one_book():
	the_url = set_the_url()
	# set the response resquests
	response = requests.get(the_url)
	# if OK, scrap the page
	if response.ok:
		product_page_url = the_url
		soup = BeautifulSoup(response.content, 'html.parser')			
		title = soup.h1.string	# scrap of title			
		image_url = urllib.parse.urljoin("http://books.toscrape.com/", soup.img['src']) # scrap of URL image			
		category = soup.find('ul')('li')[2].text.strip() # scrap gategory			
		all_p = soup.findAll('p') # find all paragraph			
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
		number_available = tds[5].text[10:12] #select only the number TODO : modif avec regex ?

		return {'product_page_url': product_page_url,
				'universal_product_code(upc)': universal_product_code,
				'title': title,
				'price_including_tax': price_including_tax,
				'price_excluding_tax': price_excluding_tax,
				'number_available': number_available,
				'product_description': product_description,
				'category': category,
				'review_rating': review_rating,
				'image_url': image_url}

try:	
	book_info = scrap_one_book()
	save_info_in_csv(book_info)
except NameError:
	print("ERREUR : Le livre est introuvable, veuillez relancer le script en vérifiant l'URL.")