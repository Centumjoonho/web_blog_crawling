import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic  # UI를 연결한다
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip


# ui 파일 연동
from_class = uic.loadUiType("blog_macro.ui")[0]


class Window(QWidget, from_class):

    input_values_soyoung_world = ['[기장 맛집] 연화반점 / 돌판짜장 / 벌집탕수육',
                                  '[울산 카페] 포레이브 frv.',
                                  '[엄궁 카페] 비상 VSANT / 부산 사상 카페',
                                  '[매화 명소] 부산 기장 매화원']

    input_values_happy_dust = ['스페인 산티아고 순례자의 길',
                               '현지업체 준투어',
                               'Oslob Whale Shark Watching Tour',
                               '투말록 폭포(Tumalog Falls)',
                               '세부공항환전소 / 막탄공항 유심',
                               '세부 호핑 투어 / 힐루뚱안, 날루수안 호핑 / 스타인월드',
                               '필리핀 입국 신고서 작성 / 제주항공 기내식',
                               '트래블로그 카드 / 환율100%우대 카드',
                               '세부 자유여행 준비 / 환전 방법']

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)

        self.comboBox.currentIndexChanged.connect(self.comboBoxFunction)
        self.btn_insert.clicked.connect(self.btn_insert_click)
        self.btn_del.clicked.connect(self.btn_del_click)
        self.btn_start.clicked.connect(self.btn_start_click)
        self.lineddit_insert.returnPressed.connect(self.apped_text)


##########################
###### 클릭 이벤트 함수 ###
##########################

    def comboBoxFunction(self):
        if self.comboBox.currentText() == '여행하는 토마토':
            self.text_browser.setText("\n".join(self.input_values_happy_dust))
        elif self.comboBox.currentText() == '토마토는 토마토':
            self.text_browser.setText(
                "\n".join(self.input_values_soyoung_world))

    def btn_insert_click(self):
        self.text_browser.append(self.lineddit_insert.text())
        self.lineddit_insert.clear()

    def btn_del_click(self):
        self.del_num()

    def btn_start_click(self):
        self.start()


###############################
############ 기능 함수 #########
###############################


    def macro_start(self, input_values):

        running_count = self.spinBox_count.value()

        print(running_count)
        if running_count <= 0:

            return self.lineddit_insert.setText("Count를 눌러주세요")

        else:
            num = 0
            while num < running_count:

                driver = webdriver.Chrome('chromedriver')
                driver.implicitly_wait(1)
                driver.get('https://www.daum.net/')

                for input_value in input_values:

                    input = driver.find_element(
                        By.CSS_SELECTOR, "[title = '검색어 입력']")

                    input.click()

                    time.sleep(1)

                    pyperclip.copy(input_value)

                    input.send_keys(Keys.CONTROL, 'v')
                    search_btn = driver.find_element(
                        By.CLASS_NAME, 'ico_pctop.btn_search')
                    search_btn.click()

                    time.sleep(1)

                    try:
                        combo_box_text = self.comboBox.currentText()
                        print(combo_box_text)
                        my_blog = driver.find_element(
                            By.LINK_TEXT, combo_box_text)
                        my_blog.click()
                        time.sleep(10)

                    except:
                        print("에러 확인")
                        pass

                    driver.back()

                time.sleep(3)

                num += 1
                print("완료 : ", num)
                driver.close()

    def start(self):

        browser_text = self.text_browser.toPlainText()

        browser_text_list = browser_text.split('\n')

        if self.comboBox.currentText() == "여행하는 토마토":

            self.input_values_happy_dust.extend(browser_text_list)
            self.macro_start(self.input_values_happy_dust)

        elif self.comboBox.currentText() == "토마토는 토마토":

            self.input_values_soyoung_world.extend(browser_text_list)
            self.macro_start(self.input_values_soyoung_world)

    def del_num(self):
        exist_text = self.text_browser.toPlainText()
        self.text_browser.setText(exist_text[:-1])

    def apped_text(self):
        self.text_browser.append(self.lineddit_insert.text())
        self.lineddit_insert.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myCalc = Window()
    sys.exit(app.exec_())
