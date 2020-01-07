import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*', 'user-agent':
    '\nMozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'} #эмулируем usera Network
base_url = 'https://hh.ru/'   #URL for parser

def hh_parse(base_url, headers):
    session = requests.Session() #создаем сесссию одного пользователя чтобы сайт думал что это чел
    request = session.get(base_url, headers = headers)
    if request.status_code == 200:
        print('OK')
    else:
        print('Error')

hh_parse(base_url, headers)