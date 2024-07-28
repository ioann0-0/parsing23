import requests
from bs4 import BeautifulSoup

# URL страницы погоды
url = 'https://yandex.kz/pogoda/astana'

response = requests.get(url)
if response.status_code == 200:
    content = response.text
    
    start = content.split('<div id="weather">')[1]
    end = start.split('</div>')[0]
    
    print('Погода в Астане:', end.strip())
else:
    print('Не удалось получить данные о погоде.')
