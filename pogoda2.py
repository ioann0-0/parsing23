import requests
from bs4 import BeautifulSoup

url = 'https://www.timeanddate.com/weather/kazakstan/astana/hourly'

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    weather_div = soup.find('div', id='weather')
    if weather_div:
        print('Погода в Астане:', weather_div.get_text(strip=True))
    else:
        print('Не удалось найти данные о погоде.')
else:
    print('Не удалось получить данные о погоде.')
