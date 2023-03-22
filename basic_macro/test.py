import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip
import requests
import time
import urllib
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get('https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=')

time.sleep(3)
query = driver.find_element(By.ID, 'q')
query.click()

query_value = '고양이'
pyperclip.copy(query_value)
query.send_keys(Keys.COMMAND, 'v')

time.sleep(3)
search_btn = driver.find_element(By.ID, 'daumBtnSearch')
search_btn.click()

img_tag = driver.find_elements(By.CLASS_NAME, 'thumb_img')

if not (os.path.isdir("./cat")):
    os.makedirs(os.path.join("./cat"))
count = 0
for item in img_tag:
    if count >= 30:
        break
    img_data = item.get_attribute('src')
    headers = {'Referer': img_data}
    img_result = requests.get(img_data, headers=headers).content
    url = "./cat/cat" + str(count).zfill(3) + ".png"
    count += 1
    with open(url, 'wb') as f:
        f.write(img_result)
driver.close()
