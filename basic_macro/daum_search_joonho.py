# 다음 통해서 진행
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
import pyperclip


hot_input_values = ['파이썬 랜덤 수 만들기', '블랜더 파이썬', '머신비전 분해능', '블랜더 blender 영상 합성', 'C# Thread 동기화',
                    'Window OS에 MongoDB', ' 네트워크 , Socket , TCP소켓 ', 'Python PyQt5로 계산기 ',
                    ' 구조분해할당(Destructing)', 'Java Spring Ajax', 'mssql cursor trigger',
                    'LINUX Maria 데이터', 'Docker Dockerfile 작성법', 'Flutter 초심자들을 위한 설치', 'iOS SwiftUI Webview 를 띄우기']


num = 0
while num < 2:

    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(1)
    driver.get('https://www.daum.net/')

    for iv in hot_input_values:

        # random_value = random.choice(hot_input_values)

        input = driver.find_element(By.CSS_SELECTOR, "[title = '검색어 입력']")

        input.click()

        time.sleep(1)

        pyperclip.copy(iv)

        input.send_keys(Keys.CONTROL, 'v')
        search_btn = driver.find_element(By.CLASS_NAME, 'ico_pctop.btn_search')
        search_btn.click()

        time.sleep(1)

        try:
            myblog = driver.find_element(By.LINK_TEXT, '센텀준호')
            myblog.click()
            time.sleep(3)

        except:
            print("에러 확인")
            pass

        driver.back()

    time.sleep(1)
    driver.close()
    num += 1
    print(f"{num} 사이클 완료")


print("전부 완료")
driver.quit()


# https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/
# 실패
# driver.find_element(By.CSS_SELECTOR, "[id='recent']").click()
# driver.find_element(By.LINK_TEXT, '" 필리핀 "').click()
# driver.find_element(By.CSS_SELECTOR, ".link_sub_item").click()
# driver.find_element(By.CLASS_NAME, 'link_tit').click()
