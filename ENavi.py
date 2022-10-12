# -*- coding: utf-8 -*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import datetime
import time
import os 

# webdriverの保存先を指定（コメントアウトすれば、~/.wdmに保存される）
os.environ['WDM_LOCAL'] = '1'

class ENavi:

    # コンストラクタ
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
        self.driver.implicitly_wait(10)

    # ログイン画面
    def enavi_login(self, URL, USER_ID, USER_PASSWORD):
        self.driver.get(URL)
        self.driver.find_element(by=By.ID, value='TextStaffNo').send_keys(USER_ID)
        self.driver.find_element(by=By.ID, value='TextPassword').send_keys(USER_PASSWORD)
        self.driver.find_element(by=By.ID, value='BtnOk').click()

    # TOP画面
    def enavi_top(self):
        self.driver.find_element(by=By.ID, value='ImgBtnMenuMonth').click()

    # 月次勤怠画面
    def enavi_month(self, DATE):
        self.driver.find_element(by=By.ID, value="LinkBtnDate" + str(int(DATE.split('/')[1]) - 1).zfill(2)).click()

    # 勤怠入力画面
    def enavi_input(self, WORK_STATUS, START_TIME, END_TIME, COMMENT):
        Select(self.driver.find_element(by=By.ID, value="CmbStatus")).select_by_index(WORK_STATUS)
        Select(self.driver.find_element(by=By.ID, value="CmbBeginTimeHour")).select_by_index(int(START_TIME.split(":")[0]))
        Select(self.driver.find_element(by=By.ID, value="CmbBeginTimeMin")).select_by_index(int(START_TIME.split(":")[1]))
        Select(self.driver.find_element(by=By.ID, value="CmbEndTimeHour")).select_by_index(int(END_TIME.split(":")[0]))
        Select(self.driver.find_element(by=By.ID, value="CmbEndTimeMin")).select_by_index(int(END_TIME.split(":")[1]))
        self.driver.find_element(by=By.ID, value="TextComment").clear()
        self.driver.find_element(by=By.ID, value="TextComment").send_keys(COMMENT)
        self.driver.find_element(by=By.ID, value="BtnOkSigndayedit").click()

    # 承認依頼確認画面
    def enavi_confirm(self):
        self.driver.find_element(by=By.ID, value="BtnOk").click()
        self.driver.switch_to.alert.accept()

    # 終了処理
    def enavi_end(self, LOG_FILE_PATH):
        time.sleep(3)
        FILENAME = str('{0:%Y%m%d_%H%M}'.format(datetime.datetime.today()))
        self.driver.save_screenshot(LOG_FILE_PATH + FILENAME + ".png")
        self.driver.quit()

    # リセット用
    def enavi_reset(self, WORK_STATUS, LOG_FILE_PATH):
        self.driver.find_element(by=By.ID, value="BtnCancelSign").click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(by=By.ID, value="-1").click()
        Select(self.driver.find_element(by=By.ID, value="CmbStatus")).select_by_index(WORK_STATUS)
