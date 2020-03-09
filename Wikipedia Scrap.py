'''Python Web Scrape Program to scrape language tab and show the name of the language for the entry'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as data

entry = int(input())
website = urlopen('https://en.wikipedia.org/')
source = BeautifulSoup(website, "html.parser")

all_lang = source.findAll('a', {'class' : 'interlanguage-link-target'})
lang_list = []
title_list = []

for name in all_lang:
    lang_sample = name.get_text()
    lang_list.append(lang_sample)
    lang_title = name.get('title')
    title_list.append(lang_title)

if (entry>len(lang_list)):
    print("Out of range")
else:
    print(lang_list[entry-1])
    print(title_list[entry-1])
