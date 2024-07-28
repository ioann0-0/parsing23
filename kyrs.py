from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = '/path/to/chromedriver'

chrome_options = Options()
chrome_options.add_argument('--headless')  

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://kase.kz/ru/currency/'  

try:
    driver.get(url)
    
    time.sleep(5)

    # Замените 'currency-rate' на реальный селектор
    rate_element = driver.find_element(By.CSS_SELECTOR, '.currency-rate','td')
    print('Курс валют:', rate_element.text)
finally:
    driver.quit()
