import requests
from bs4 import BeautifulSoup

def request_page(url):
    '''Makes a request to the website and saves the HTML in BS format'''
    # request to the page
    page = requests.get(url)
    # extract the test
    soup = BeautifulSoup(page.content, 'lxml')
    return soup