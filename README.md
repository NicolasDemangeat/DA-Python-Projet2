# Scraping "books.toscrape.com"
Application de scraping pour le site http://books.toscrape.com.

## *Table des matières*
1. [Prérequis](#1-prérequis)
2. [Informations générales](#2-informations-générales)
   - [scraping_one_book.py](#a-scraping_one_bookpy)
   - [scraping_one_category.py](#b-scraping_one_categorypy)
   - [scraping_all_category.py](#c-scraping_all_categorypy)
3. [Exécuter les scripts](#3-exécuter-les-scripts)
4. [Analyse du résultat](#4-analyse-du-résultat)
5. [Futures améliorations](#5-futures-améliorations)
6. [Auteur](#6-auteur)

## 1. Prérequis
Pour pouvoir exécuter les scripts il nécessaire d'installer la version 3.9.0 de python : 
https://www.python.org/downloads/release/python-390/

## 2. Informations générales
  Ce repository contient trois scripts qui ont chacun un rôle différent.

Le but final est d'aller récupérer sur le site https://books.toscrape.com/ un certain nombre d'informations concernant les livres et de télécharger l'image de couverture des livres.

  Ces informations sont : 
- product_page_url 
- universal_product_code(upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

### A) scraping_one_book.py
Le script "scraping_one_book.py" va récupérer les informations et l'image pour un seul livre.  
Le script va créer un dossier "Books-To-Scrape" contenant le résultat de l'exécution du script.  
Il sera demandé lors de l'exécution du script de renseigner *l'URL d'un livre*. Il suffit donc de faire un copier/coller de *l'URL d'un livre*.  
Par exemple : https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html

### B) scraping_one_category.py
Le script "scraping_one_category.py" va récupérer les informations et les images pour tous les livres d'une catégorie.  
Le script va créer un dossier "Books-To-Scrape" contenant le résultat de l'exécution du script.  
Il sera demandé lors de l'exécution du script de renseigner *l'URL d'une catégorie* de livre. Il suffit donc de faire un copier/coller de *l'URL de la catégorie*.  
Par exemple : https://books.toscrape.com/catalogue/category/books/travel_2/index.html

### C) scraping_all_category.py
Le script "scraping_all_category.py" va récupérer les informations et les images pour tous les livres de toutes les catégories, ce qui correspond à tous les livres du site.  
Le script va créer un dossier "Books-To-Scrape" contenant le résultat de l'exécution du script.  
Il s'exécute sans demander de renseigner d'URL.  

## 3. *Exécuter les scripts*
Après avoir téléchargé DA-Python-Projet2-main.zip depuis GitHub, il faut l'extraire dans un dossier de votre choix.   
Ensuite, en utilisant l'invite de commandes Windows (ou le terminal si vous êtes sur Mac ou Linux) :  
- Placez vous dans le dossier  
- Créez un environnement virtuel  
- Activez le  
- Installez les modules depuis requirements.txt
```
$ CD ../chemin/vers/DA-Python-Projet2-main
$ python -m venv env
$ env\Scripts\activate
$ pip install -r requirements.txt
```
Vous pouvez maintenant exécuter le script de votre choix en tapant l'une des commandes suivante.
```
$ python scraping_one_book.py
```
ou
```
$ python scraping_one_category.py
```
ou
```
$ python scraping_all_category.py
```

## 4. *Analyse du résultat*
Par exemple, après avoir exécuter ```$ python scraping_one_book.py```, un dossier "Books-To-Scrape" est créer dans le dossier courant.  

Le dossier "Books-To-Scrape" se décompose comme suit :
- Dossier : "Books-To-Scrape"
   - Dossier : "Nom-de-la-catégorie-du-livre"
      - Fichier : Image de couverture du livre
      - Fichier : "Nom-de-la-catégorie-du-livre" .csv

Le formatage du résultat reste le même pour chaque script. 

Ainsi, pour ```$ python scraping_one_category.py``` le dossier "Books-To-Scrape" va contenir un sous dossier "Nom-de-la-catégorie" contenant les images de couverture des livres et le fichier .csv.  

Pour ```$ python scraping_all_category.py``` le dossier "Books-To-Scrape" va contenir autant de sous-dossier "Nom-de-la-catégorie" que de catégories sur le site, c'est à dire cinquante.

## 5. *Futures améliorations*
Voici une liste des améliorations envisageable :
- Faire une interface graphique (ou web)
- Réécriture en fonction asynchrone pour améliorer la vitesse d'exécution
- Lancer un seul script qui nous donne le choix entre les trois déjà existant

## 6. *Auteur*
- Nicolas Demangeat > Profil : [CodeWars](https://www.codewars.com/users/Morkai) - [CodinGame](https://www.codingame.com/profile/12632339c7b1539aedc9bb480ed2cac44538993)
