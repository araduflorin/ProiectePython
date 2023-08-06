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
# driver.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/")
# driver.find_element(By.CLASS_NAME, 'swal2-confirm').click()
# rows = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr"))
# rows = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr"))
# print(rows)
# r = ''
# for i in range(1, rows):
#     row1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[" + str(rows) + "]").text
#     r = row1
# # print(r)
#
# # row1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[" + str(r) + "]").text
# # row1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[last()]").text
# print("Ultima linie:", r)

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
    cols_last_row = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr["+ str(rows) +"]/td"))
    # print(cols_last_row)
    # last_row = ''
    # l = []
    # # for row in range(1, rows+1):
    # for p in range(1, cols):
    #     for row in range(1, rows + 1):
    #         last_row = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[" + str(rows) + "]/td[" + str(p) + "]").text
    #         r=last_row
    #     l.append(last_row)
    # print(type(l))
    # print(len(l))
    # print(l[0:2])

    lst = []
    # row1 = ''
    for r in range(2, rows+1):
        for p in range(1, cols - 1):
            value = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[" + str(r) + "]/td[" + str(p) + "]").text
            # row1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[-1]").text
            lst.append(value)
            # list_row.append(last_row)
        # lst.append(row)
    # print(lst)
    # lst.append(l[0:2])
    # del lst[-2:-4]
    print("Lista: ", lst)
    return lst
# time.sleep(2)

# # Obtain the number of columns in table
# cols = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td"))
# list_col = driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td")
# Print rows and columns
link1 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/')
link2 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00-2/')
link3 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00-2/')
link4 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-3/')
link5 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/')

# print(link1)
# print(link2)
# print(link3)
# print(link4)
# print(link5)
# # print(link1[1])
# # print(link1[2])
# print(type(link1))
# # print(cols)

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
        # dic[link1[i], link1[i+1]] = [link1[i+2], link2[i+2], link3[i+2], link4[i+2], link5[i+2]]
        # dic.add[link1[i], link1[i+1], link1[i+2], link2[i+2], link3[i+2], link4[i+2], link5[i+2]]
    dic[i] = [link1[i], link1[i+1], link1[i+2], link2[i+2], link3[i+2], link4[i+2], link5[i+2]]
print(dic)
list_header = ['Nr.Crt','Judet','01.03','02.03','03.03','04.03','05.03']
# pd.options.display.float_format = '{:,.2f}'.format
df = pd.DataFrame(dic).transpose()
# df.head(list_header)
# df.columns=list_header
        # df = pd.DataFrame(dic).transpose()
        # df.reset_index(drop=True)
        # df = pd.DataFrame(lst)
#


update_df = df.drop([df.index[-2], df.index[-3]])
update_df.to_csv('Covid_data.csv', sep='|', header=list_header, index=False)


