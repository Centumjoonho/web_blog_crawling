# 다음 통해서 진행
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pyperclip


driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.daum.net/')

time.sleep(1)

input = driver.find_element(By.CSS_SELECTOR, "[title = '검색어 입력']")

input.click()

time.sleep(2)

input_value = '[필리핀] 세부 오슬롭 고래상어 투어 / Oslob Whale'
pyperclip.copy(input_value)

input.send_keys(Keys.CONTROL, 'v')
search_btn = driver.find_element(By.CLASS_NAME, 'ico_pctop.btn_search')
search_btn.click()

time.sleep(1)

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# items = soup.select("")

# 다음은 li -> class 로 고유 값 확인 필 !

# my_blog = driver.find_element(By.CLASS_NAME, 'scrollWrapper.ty_next')
# my_blog = driver.find_element(
#     By.CSS_SELECTOR, "[href='http://soyoungworld.tistory.com/82']")

for i in range(82, 100):
    my_blog_all = driver.find_element(
        By.CSS_SELECTOR, f"[href='http://soyoungworld.tistory.com/{i}']")
    print("안녕", my_blog_all)
    if my_blog_all:
        my_blog_all.click()
    else:
        pass


# print("My_Blog_data : ", my_blog)


time.sleep(10)
