# 다음 통해서 진행
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pyperclip


driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(1)
driver.get('https://www.daum.net/')

input_values = ['스페인 산티아고 순례자의 길',
                '현지업체 준투어',
                'Oslob Whale Shark Watching Tour',
                '투말록 폭포(Tumalog Falls)',
                '세부공항환전소 / 막탄공항 유심',
                '세부 호핑 투어 / 힐루뚱안, 날루수안 호핑 / 스타인월드',
                '필리핀 입국 신고서 작성 / 제주항공 기내식',
                '트래블로그 카드 / 환율100%우대 카드',
                '세부 자유여행 준비 / 환전 방법']
num = 0
while num < 10:

    for iv in input_values:

        input = driver.find_element(By.CSS_SELECTOR, "[title = '검색어 입력']")

        input.click()

        time.sleep(1)

        pyperclip.copy(iv)

        input.send_keys(Keys.CONTROL, 'v')
        search_btn = driver.find_element(By.CLASS_NAME, 'ico_pctop.btn_search')
        search_btn.click()

        time.sleep(1)

        try:
            myblog = driver.find_element(By.LINK_TEXT, '여행하는 토마토')
            myblog.click()
            time.sleep(3)

        except:
            print("에러 확인")
            pass

        driver.back()
        
# https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/
    # 실패
    # driver.find_element(By.CSS_SELECTOR, "[id='recent']").click()
    # driver.find_element(By.LINK_TEXT, '" 필리핀 "').click()
    # driver.find_element(By.CSS_SELECTOR, ".link_sub_item").click()
    # driver.find_element(By.CLASS_NAME, 'link_tit').click()

    time.sleep(10)
    num += 1
    print("완료 : ", num)
