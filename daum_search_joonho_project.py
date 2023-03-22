# 다음 통해서 진행
import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# 저장 경로
current_path = os.getcwd()
# 원하는 검색어 및 이미지 개수
inserturl = input("검색어를 입력하세요 : ").strip()
img_num = input("원하는 이미지 개수 입력하세요 : ").strip()

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)
driver.get(f'https://search.daum.net/search?w=img&q={inserturl}')
driver.maximize_window()

time.sleep(3)

# 현재 브라우저의 높이
last_height = driver.execute_script(
    "return document.body.scrollHeight")  # 브라우져 높이를 확인 가능(자바스크립트)

# 검색 화면에서 스크롤을 끝까지 내려 관련 이미지 전부를 가져옵니다.
while True:
    # Scroll down to bottom
    # 브라우져 끝까지 스크롤을 내리겠다.
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(new_height)

    if new_height == last_height:
        try:
            # 화면 맨 아래 펼쳐보기 버튼 클릭
            search_more = driver.find_element(
                By.CSS_SELECTOR, ".expender.open")
            search_more.click()
            time.sleep(2)
        except:
            print("error")
            break
    last_height = new_height

# 복수 이미지 정보를 가져옵니다 list 형  * find_elements 를 사용합니다.
images = driver.find_elements(By.CSS_SELECTOR, ".thumb_img")

# 폴더 명도 검색어랑 동일하게 세팅 !
folder_name = inserturl
# 폴더 있는지 없는지 확인 후 생성
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
# 원하는 개수의 이미지만 다운로드 !
img_count = 1
for image in images:

    if img_count > int(img_num):
        break
    else:
        try:
            # 이미지 다운에 중요한 src 값 가져오기
            img_url = image.get_attribute('src')
            time.sleep(1)
            # urllib.request— URL 열기를 위한 확장 가능한 라이브러리  검색해서 사용법 숙지
            urllib.request.urlretrieve(
                img_url, folder_name + "/" + inserturl + "." + str(img_count) + ".jpg")
            img_count += 1
        except:
            print("error")
            pass
driver.close()
