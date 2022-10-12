# -*- coding: utf-8 -*-

import traceback
import ENavi
import datetime

# 定数
URL = "https://hogehoge"
USER_ID = "hgoehgo"
USER_PASSWORD = "hogehoge"
DATE = datetime.datetime.now().strftime("%m/%d")
LOG_FILE_PATH = "./log/"
START_TIME = "09:00"
END_TIME = "18:00"
WORK_STATUS = "0"
COMMENT = "在宅勤務"

def main():
    try:
        # ENaviクラスのインスタンス化
        enavi = ENavi.ENavi()
        print("インスタンス化\t：OK")
        # ログイン画面
        enavi.enavi_login(URL, USER_ID, USER_PASSWORD)
        print("ログイン\t：OK")
        # トップ画面
        enavi.enavi_top()
        print("トップ画面\t：OK")
        # 月次勤怠画面
        enavi.enavi_month(DATE)
        print("月次勤怠画面\t：OK")
        # 勤怠入力画面
        enavi.enavi_input(WORK_STATUS, START_TIME, END_TIME, COMMENT)
        print("勤怠入力画面\t：OK")
        # 承認依頼画面
        enavi.enavi_confirm()
        print("承認依頼画面\t：OK")
        print("TOTAL\t\t：正常終了")
    # 例外処理
    except Exception as e:
        print("こけた")
        print(e)
        print(traceback.format_exc())
    # 終了処理
    finally:
        enavi.enavi_end(LOG_FILE_PATH)

if __name__ == "__main__":
    main()
