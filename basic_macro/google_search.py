# 네이버 통해서 진행
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import pyperclip

my_url = 'smart-factory-lee-joon-ho.tistory.com'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://google.com/')
driver.maximize_window()
action = ActionChains(driver)
# 로그인 버튼
driver.find_element(By.CSS_SELECTOR, ".gb_ie").click()
# 로그인 아이디
action.send_keys('ghwnsgkgkgk@gmail.com').perform()
# 다음 버튼
# driver.find_element(By.CSS_SELECTOR, "[type='button']").click()


time.sleep(50)

# driver.find_element(By.XPATH, '//button[text()="Some text"]')
# driver.find_element(By.XPATH, '//button')
# driver.find_element(By.ID, 'loginForm')
# driver.find_element(By.LINK_TEXT, 'Continue')
# driver.find_element(By.NAME, 'username')
# driver.find_element(By.TAG_NAME, 'h1')
# driver.find_element(By.CLASS_NAME, 'content')
# driver.find_element(By.CSS_SELECTOR, 'p.content’)
# driver.find_elements(By.ID, 'loginForm')
# driver.find_elements(By.CLASS_NAME, 'content')
# [출처] 3/18 크롤링 데이터수집 - 이경용 (AI클럽 (aiclub.kr)) | 작성자 이경용
