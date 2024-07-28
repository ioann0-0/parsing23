from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = 'C:/'

chrome_options = Options()
chrome_options.add_argument('--headless')  
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://kaspi.kz/shop/almaty/' 

try:
    driver.get(url)
    
    time.sleep(5)
    
    price_elements = driver.find_elements(By.CSS_SELECTOR, '.price','#span')
    
    prices = [price_element.text for price_element in price_elements]
    
    for price in prices:
        print('Цена:', price)
finally:
    driver.quit()
