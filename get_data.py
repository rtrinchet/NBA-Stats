import requests
from bs4 import BeautifulSoup

import string
import pandas as pd

def request_page(url):
    '''Makes a request to the website and saves the HTML in BS format'''
    # request to the page
    page = requests.get(url)
    # extract the test
    soup = BeautifulSoup(page.content, 'lxml')
    return soup


def extract_player_info(player_text, b_url = 'https://www.basketball-reference.com'):
    url = b_url + player_text.a['href']
    name = player_text.a.text
    info = [name, url]
    info.extend([elem.text for elem in player_text.find_all('td')])
    return info


def df_from_url(url):
    players_soup = request_page(url)
    
    cols = [elem.text.lower() for elem in players_soup.find('thead').find_all('th')]
    cols.insert(0, "url")
    
    a_players = players_soup.find('tbody').find_all('tr')
    result = [extract_player_info(player_text) for player_text in a_players]

    df = pd.DataFrame(result, columns = cols)
    
    return df

def get_players_data(players_url='https://www.basketball-reference.com/players/'):
    
    alphabet = list(string.ascii_lowercase)
    list_urls = [players_url + letter + '/' for letter in alphabet]
    df0 = df_from_url(list_urls[0])
    
    df_list = [df_from_url(url) for url in list_urls]
    df = pd.concat(df_list, axis = 0)
    print(df.shape)
    return df