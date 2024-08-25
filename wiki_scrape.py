'''This file scrapes text from popular wikipedia pages using the wiki api and beautiful soup'''
import wikipediaapi
from bs4 import BeautifulSoup
import requests
import re
import shutil

wiki_wiki = wikipediaapi.Wikipedia('My_Proj','en') # creating wiki api env

url = "https://en.wikipedia.org/wiki/Wikipedia:Popular_pages" # page containing 100 most popular wikipedia searches

response = requests.get(url) 

soup = BeautifulSoup(response.content,'html.parser')

top_categories_table = soup.find_all("table", class_="wikitable") # selecting list of top pages by specific categories

num_tags = 0
target_directory = "pages"

for list in top_categories_table: 
    list_tags = list.find_all('a') # finding all links in tables and extracting text
    for tag in list_tags:
        if not re.search(r'\[', tag.text) and len(wiki_wiki.page(tag.text).text) > 1000: # parsing out bracket elements with no searchable page
            filename = "page" + str(num_tags) + ".txt"
            with open(filename, "w", encoding='utf-8') as f: # writing wikipedia page content to .txt file
                f.write(wiki_wiki.page(tag.text).text)
            shutil.move(filename, target_directory) # move file to pages directory

