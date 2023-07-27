import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import selenium.common.exceptions as exceptions
import pandas as pd
import csv

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/')
table = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody')
table1 = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[4]')

lista = table.text.split('\n')
lista1 = table.text.split('\n')
print(lista)
print(lista1)

# get_element = driver.find_element(by=By.ID, value='searchboxTrigger')
# get_element.send_keys('telefon')
# # time.sleep(10)
# get_element.submit()
# element = driver.find_elements(by=By.CLASS_NAME, value='card-item')
# # print(element.text)
# list_of_elements, product_list, price_list = [], [], []
# for i in element:
#     try:
#         product = i.find_element(by=By.CLASS_NAME, value='card-v2-title-wrapper')
#         product_list.append(product.text)
#         price = i.find_element(by=By.CLASS_NAME, value='product-new-price')
#         price_list.append(price.text)
#         # print(price.text)
#
#     except exceptions.NoSuchElementException:
#         pass
# print(product_list)
# list_of_elements.append(product_list)
# list_of_elements.append(price_list)
# print(list_of_elements)
#
# # with open('emag_products.csv', 'w') as file:
# #     variabila = csv.writer(file, delimiter='|')
# #     variabila.writerows(list_of_elements)
# df = pd.DataFrame(list_of_elements).transpose()
# df.to_csv('emag_all_products.csv', sep='|')

