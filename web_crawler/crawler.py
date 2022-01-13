"""
crawler.py
This web crawler is built as part of BTON project to crawl over
Bennington College offical website (www.bennington.edu). It uses 
BeautifulSoup module of python to extract employee data from 
different offices of Bennington college.

Tesfatsion Shiferaw
2022 G.C
"""
from unittest.main import main
import requests
from bs4 import BeautifulSoup

from utility import write_json

def word_cleanup(word):
    """removes blank and new line space from a word"""
    return word.strip(' ').strip('\n')

def presidents_office(url_list, main_website='https://www.bennington.edu'):
    """scraps through the presidents office site on bennington.edu
    Args:
    main_website: url of the main webiste. In this case, https://www.bennington.edu
    url: list of specific site extensions to be scrapped with out the main website. 
         For https://www.bennington.edu/technology, enter [technology, ...]
    Returns:
    writes the data to json file
    """
    for extension in url_list:
        data = [] # store all the information here
        full_url = main_website + '/' + extension
        print(full_url)
        source_code = requests.get(full_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('div', {'class': 'person-detail-box'}):
            dict_ = {}
            dict_['name'] = word_cleanup(link.h5.text)
            dict_['img_src'] = main_website + link.img['src']
            count = 0 # keep track of what comes first and second
            for small_link in link.findAll('div'):
                word = word_cleanup(small_link.text)
                if count == 0:
                    dict_['position'] = word
                    count += 1
                else:
                    dict_['location'] = word
            data.append(dict_)
        write_json(data, extension)

if __name__ == '__main__':
    url_list = ['admissions-office', 'presidents-office', 'technology', 'business-office' ]
    presidents_office(url_list)

