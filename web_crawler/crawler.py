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

def spider(url_list, main_website='https://www.bennington.edu', separate_files=False):
    """scraps through the presidents office site on bennington.edu
    Args:
    url: string, list of specific site extensions to be scrapped with out the main website. 
         For https://www.bennington.edu/technology, enter [technology, ...]
    main_website: string, url of the main webiste. In this case, https://www.bennington.edu
    all_in_one: bool, create a separate file for each scrapped page.
    Returns:
    writes the data to json file
    """
    # set up logging
    # Creating an object
    all_data = [] # store scrapped data of all office (page) here, if all_in_one is enabled
    for extension in url_list:
        data = [] # store scrapped data of a single office (page) here
        full_url = main_website + '/' + extension

        print("Crawling over", full_url)
        try:
            source_code = requests.get(full_url)
        except requests.exceptions.RequestException as e:  # handle errors
            raise SystemExit(e)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('div', {'class': 'person-detail-box'}):
            dict_ = {}
            dict_['name'] = word_cleanup(link.h5.text)
            dict_['img_src'] = main_website + link.img['src']
            dict_['page'] = extension
            count = 0 # keep track of what comes first and second
            for small_link in link.findAll('div'):
                word = word_cleanup(small_link.text)
                if count == 0:
                    dict_['position'] = word
                    count += 1
                else:
                    dict_['location'] = word
            all_data.append(dict_)
            if separate_files:
                data.append(dict_)
        if separate_files:
            write_json(data, extension)
    write_json(all_data, 'all_scraped_data')

if __name__ == '__main__':
    url_list = ['admissions-office', 'presidents-office', 'technology', 'business-office' ]
    spider(url_list, separate_files=True)

