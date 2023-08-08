from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")


def get_link(link):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get(link)
    driver.find_element(By.CLASS_NAME, 'swal2-confirm').click()
    rows = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr"))
    cols = len(
        driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[1]/td"))

    list_data = []
    for r in range(2, rows + 1):
        for c in range(1, cols - 1):
            value = driver.find_element(By.XPATH,
                                        "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[" + str(
                                            r) + "]/td[" + str(c) + "]").text
            list_data.append(value)
    return list_data


link1 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/')
link2 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00-2/')
link3 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00-2/')
link4 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-3/')
link5 = get_link('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/')

dic_data = {}
for i in range(0, len(link1), 3):
    dic_data[i] = [link1[i], link1[i + 1], link1[i + 2], link2[i + 2], link3[i + 2], link4[i + 2], link5[i + 2]]

total_row1 = link1[-2]
total_row2 = link2[-2]
total_row3 = link3[-2]
total_row4 = link4[-2]
total_row5 = link5[-2]

list_header = ['Nr.Crt', 'Judet', '01.03', '02.03', '03.03', '04.03', '05.03']

df = pd.DataFrame(dic_data).transpose()
df_update = df.drop([df.index[-1], df.index[-2], df.index[-3]])
df_update.loc[(df.index[-3])] = ['', 'TOTAL', ''.join(total_row1), ''.join(total_row2), ''.join(total_row3),
                                 ''.join(total_row4), ''.join(total_row5)]
df_update.to_csv('Covid_data.csv', sep='|', header=list_header, index=False)
