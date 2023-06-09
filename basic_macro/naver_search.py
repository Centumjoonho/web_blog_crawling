# 네이버 통해서 진행
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import pyperclip

my_url = 'smart-factory-lee-joon-ho.tistory.com'
driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get('https://naver.com/')
driver.maximize_window()
action = ActionChains(driver)

time.sleep(1)

# CSS_SELECTOR
# id -> # class -> .
#"[title = '검색어 입력']"
input = driver.find_element(By.CSS_SELECTOR, "[title = '검색어 입력']")
input.click()

time.sleep(1)

input_value = 'BLENDER : PYTHON 블랜더 파이썬으로 코딩하여 플러그인 개발하기'
pyperclip.copy(input_value)
input.send_keys(Keys.CONTROL, 'v')

time.sleep(1)

search_btn = driver.find_element(By.ID, 'search_btn')
search_btn.click()

time.sleep(3)


# a 태그 특정 link 값으로 연결)
# https://0433.tistory.com/41
my_blog = driver.find_element(
    By.LINK_TEXT, f'{my_url}')

my_blog.click()

time.sleep(3)


# driver.find_element(By.XPATH, '//button[text()="Some text"]')
# driver.find_element(By.XPATH, '//button')
# driver.find_element(By.ID, 'loginForm')
# driver.find_element(By.LINK_TEXT, 'Continue')
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
# driver.find_element(By.NAME, 'username')
# driver.find_element(By.TAG_NAME, 'h1')
# driver.find_element(By.CLASS_NAME, 'content')
# driver.find_element(By.CSS_SELECTOR, 'p.content’)
# driver.find_elements(By.ID, 'loginForm')
# driver.find_elements(By.CLASS_NAME, 'content')
# [출처] 3/18 크롤링 데이터수집 - 이경용 (AI클럽 (aiclub.kr)) | 작성자 이경용
