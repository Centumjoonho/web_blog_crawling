# 다음 통해서 진행
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import random

input_values = ['[기장 맛집] 연화반점 / 돌판짜장 / 벌집탕수육',
                '[울산 카페] 포레이브 frv.',
                '[엄궁 카페] 비상 VSANT / 부산 사상 카페',
                '[매화 명소] 부산 기장 매화원',
                '부산하우스열무국수',
                '수영 돼지국밥 주차장 정보',
                '오스트리아 빈 벨베데레 궁전 살람 브로우',
                '오스트리아 빈 빈시청사 뉴이어마켓',
                '부산 전포 카페 차르콜 CHAR COAL',
                '영알종주 9봉 완등 인증서',
                '실업급여신청 고용보험 이직확인서',
                '파우제앤숨 식물원 카페 부산근교 카페',
                '제주도종주 제주도 자전거 종주 제주도 라이딩',
                ]

print(random.choice(input_values))
num = 0
while num < 10:

    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(1)
    driver.get('https://www.daum.net/')

    for i in input_values:

        random_value = random.choice(input_values)
        input = driver.find_element(By.CSS_SELECTOR, "[title = '검색어 입력']")

        input.click()

        time.sleep(1)

        pyperclip.copy(random_value)

        input.send_keys(Keys.CONTROL, 'v')
        search_btn = driver.find_element(By.CLASS_NAME, 'ico_pctop.btn_search')
        search_btn.click()

        time.sleep(1)

        try:
            my_blog = driver.find_element(By.LINK_TEXT, '토마토는 토마토')
            my_blog.click()
            time.sleep(20)

        except:
            print("에러 확인")
            pass

        driver.back()

    time.sleep(3)

    num += 1
    print("완료 : ", num)
    driver.close()
