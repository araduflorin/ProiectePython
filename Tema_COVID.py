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
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
# driver.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/')
# rows = driver.fin("//*[@id='proxylisttable']/tbody/tr")

# driver.find_element(By.CLASS_NAME, 'swal2-confirm').click()
def get_link(link):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get(link)
    driver.find_element(By.CLASS_NAME, 'swal2-confirm').click()
    rows = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr"))
    cols = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td"))
    lst=[]
    for r in range(2, rows - 2):
        for p in range(1, cols - 1):
            value = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[" + str(r) + "]/td[" + str(p) + "]").text
            lst.append(value)
    return lst
# time.sleep(2)
# table = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[1]/main/article/div/div/table/tbody/tr['+'10'+']')
# table = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[11]')
# table1 = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[2]/td[1]')

# lista = table.text.split('\n')
# lista1 = table1.text.split('\n')
# print(lista)
# print(lista1)

# rows = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr"))
#
# # Obtain the number of columns in table
# cols = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td"))
# list_col = driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td")
# Print rows and columns
link1 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/')
link2 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00-2/')

print(link1)
print(link2)
# print(link1[1])
# print(link1[2])
print(type(link1))
# print(cols)

# Printing the table headers
# print("Locators           " + "             Description")

# lst = []
dic = {}
# Printing the data of the table
# for r in range(2, rows - 2):
#     for p in range(1, cols - 1):
#         # obtaining the text from each column of the table
#         # value = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[" + str(r) + "]/td[" + str(p) + "]").text
#         lst.append(value)
#         # for i in range(0, len(lst), 2):
#         #     dic[lst[i]] = lst[i+1]
#         print(value, end='       ')
#     print()
# print(lst)
for i in range(0, len(link1), 3):
        dic[link1[i], link1[i+1]] = link1[i+2]
print(dic)
df = pd.DataFrame(dic, index=[0]).transpose()
        # df = pd.DataFrame(dic).transpose()
        # df.reset_index(drop=True)
        # df = pd.DataFrame(lst)
df.to_csv('Covid_data.csv', sep='|')

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