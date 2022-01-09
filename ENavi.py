# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import datetime

class ENavi:

    # コンストラクタ
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)

    # ログイン画面
    def enavi_login(self, URL, USER_ID, USER_PASSWORD):
        self.driver.get(URL)
        self.driver.find_element_by_id('TextStaffNo').send_keys(USER_ID)
        self.driver.find_element_by_id('TextPassword').send_keys(USER_PASSWORD)
        self.driver.find_element_by_id('BtnOk').click()

    # TOP画面
    def enavi_top(self):
        self.driver.find_element_by_id('ImgBtnMenuMonth').click()

    # 月次勤怠画面
    def enavi_month(self, DATE):
        self.driver.find_element_by_id("LinkBtnDate" + str(int(DATE.split('/')[1]) - 1).zfill(2)).click()

    # 勤怠入力画面
    def enavi_input(self, WORK_STATUS, START_TIME, END_TIME, COMMENT):
        Select(self.driver.find_element_by_id("CmbStatus")).select_by_index(WORK_STATUS)
        Select(self.driver.find_element_by_id("CmbBeginTimeHour")).select_by_index(int(START_TIME.split(":")[0]))
        Select(self.driver.find_element_by_id("CmbBeginTimeMin")).select_by_index(int(START_TIME.split(":")[1]))
        Select(self.driver.find_element_by_id("CmbEndTimeHour")).select_by_index(int(END_TIME.split(":")[0]))
        Select(self.driver.find_element_by_id("CmbEndTimeMin")).select_by_index(int(END_TIME.split(":")[1]))
        self.driver.find_element_by_id("TextComment").send_keys(COMMENT)
        self.driver.find_element_by_id("BtnOkSigndayedit").click()

    # 承認依頼確認画面
    def enavi_confirm(self):
        self.driver.find_element_by_id("BtnOk").click()
        Alert(self.driver).accept()
        self.driver.save_screenshot(str(datetime.datetime.now().strftime('%Y%m%d_%H%M')) + ".png")

    # 終了処理
    def enavi_end(self):
        self.driver.quit()
