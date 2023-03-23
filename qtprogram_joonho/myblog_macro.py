import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic  # UI를 연결한다
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import pyautogui


# ui 파일 연동
from_class = uic.loadUiType("blog_macro.ui")[0]


class Window(QWidget, from_class):
    ad_click_times = 0
    input_values = []

    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)

        self.text_browser.setText("\n".join(self.input_values))

        self.btn_insert.clicked.connect(self.btn_insert_click)
        self.btn_del.clicked.connect(self.btn_del_click)
        self.btn_del_all.clicked.connect(self.btn_del_click_all)
        self.btn_start.clicked.connect(self.btn_start_click)
        self.lineddit_insert.returnPressed.connect(self.apped_text)


##########################
###### 클릭 이벤트 함수 ###
##########################


    def btn_insert_click(self):
        if self.lineddit_insert.text():
            self.text_browser.append(self.lineddit_insert.text())
            self.lineddit_insert.clear()

    def btn_del_click(self):
        self.del_contents()

    def btn_del_click_all(self):
        self.del_contents_all()

    def btn_start_click(self):
        self.start()


###############################
############ 기능 함수 #########
###############################


    def macro_start(self, input_values):

        running_count = self.spinBox_count.value()
        speed_setting = self.spinBox_count_speed.value()

        if running_count == 0:

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
                        blog_name = self.textEdit.toPlainText()
                        my_blog = driver.find_element(
                            By.LINK_TEXT, blog_name)

                        my_blog.click()
                        time.sleep(2)
                        # 광고 클릭
                        self.add_click_m_s_money(speed_setting)

                    except Exception as e:
                        print("에러 확인 : ", e)
                        pass

                    driver.back()

                time.sleep(3)

                num += 1
                print(f" 완료 :{num}")
                driver.close()

    def start(self):

        browser_text = self.text_browser.toPlainText()

        browser_text_list = browser_text.split('\n')

        blog_name = self.textEdit.toPlainText()

        if self.spinBox_count.value() and blog_name:

            self.input_values.extend(browser_text_list)
            self.lineddit_insert.clear()
            self.macro_start(self.input_values)

        else:
            return self.lineddit_insert.setText("블로그 or 횟수 확인 요망")
        #########################
        print("놓친 횟수 : ", self.click_check_ad.count(None))
        print("list 내용  :", self.click_check_ad)
        self.text_browser.setText(
            f" 예상 광고 클릭 횟수 : {len(self.input_values) * self.spinBox_count.value()} 회\n 성공 광고 클릭 횟수 : {(self.ad_click_times) -(self.click_check_ad.count(None))} 회")

    def del_contents(self):
        exist_text = self.text_browser.toPlainText()
        self.text_browser.setText(exist_text[:-1])

    def del_contents_all(self):
        self.text_browser.clear()

    def apped_text(self):
        self.text_browser.append(self.lineddit_insert.text())
        self.lineddit_insert.clear()

    #############
    ## 광고클릭 ##
    #############
    click_check_ad = []

    def add_click_m_s_money(self, speed_setting):

        try:
            adfit = pyautogui.locateCenterOnScreen(
                'img_click/adfit_arrow.png', grayscale=True, confidence=0.6)
            pyautogui.click(adfit)

            time.sleep(1)
            #############
            # 마우스 이동#
            pyautogui.moveTo(1808, 46)

            time.sleep(1)

            # 실제 클릭 횟수
            self.ad_click_times += 1
            # 실패 클릭 횟수
            self.click_check_ad.append(adfit)

        except Exception as e:
            print("에러확인 : ", e)
            pass

        # try:
        #     adsense_black = pyautogui.locateCenterOnScreen(
        #         'img_click/adsense_black.png', grayscale=True, confidence=0.3)
        #     pyautogui.click(adsense_black)
        #     self.ad_click_times += 1
        #     time.sleep(1)

        # except Exception as e:
        #     print("에러확인 : ", e)
        #     pass

        ##############
        time.sleep(speed_setting)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myCalc = Window()
    sys.exit(app.exec_())
