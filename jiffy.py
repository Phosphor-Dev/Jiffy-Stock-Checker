import time

from tabulate import *

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def getInfo():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--log-level=3')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    colors = ["Heather Gray", "Pale Pink", "Royal", "Navy", "Sandshell", "Sea Foam", "White"]
    baseUrl = "https://www.jiffy.com/laneseven-LS14004.html?ac="
    driver = webdriver.Chrome(options=options)

    final = []
    for color in colors:
        data = []
        url = baseUrl + color
        driver.get(url)
        time.sleep(1)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "lxml")
        stats = soup.findAll("div", class_="product-details-quantity-form-row__form-group")
        for stat in stats:
            text = stat.text.strip().replace(' ', '').split('\n')
            text.remove('Jiffy1st')
            while '' in text:
                text.remove('')
            data.append(dict([text]))
        final.append(data)
    return final

def display(data):
    for stock in data: #insert
        sizes = ['XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', 'OSFM']
        for item in stock:
            for key in item:
                if key in sizes:
                    sizes.remove(key)
        if sizes != []:
            for size in sizes:
                stock.append({size:'N/A'})

    headers = ["Size", "Heather Gray", "Pale Pink", "Royal", "Navy", "Sandshell", "Sea Foam", "White"]
    xs = ['XS']
    s = ['S']
    m = ['M']
    l = ['L']
    xl = ['XL']
    xl2 = ['2XL']
    xl3 = ['3XL']
    osfm = ['OSFM']

    for stockList in data:
        for pair in stockList:
            for key in pair:
                if key == 'XS':
                    xs.append(pair[key])
                if key == 'S':
                    s.append(pair[key])
                if key == 'M':
                    m.append(pair[key])
                if key == 'L':
                    l.append(pair[key])
                if key == 'XL':
                    xl.append(pair[key])
                if key == '2XL':
                    xl2.append(pair[key])
                if key == '3XL':
                    xl3.append(pair[key])
                if key == 'OSFM':
                    osfm.append(pair[key])
    table = [headers, xs, s, m, l, xl, xl2, xl3, osfm]
    print(tabulate(table, headers = 'firstrow',  tablefmt='fancy_grid'))

display(getInfo())
input()
