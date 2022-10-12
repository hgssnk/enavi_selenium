# -*- coding: utf-8 -*-

import traceback
import ENavi
import datetime

# 定数
URL = "https://hgoehoge"
USER_ID = "hogehoge"
USER_PASSWORD = "hgoehoge"
DATE = datetime.datetime.now().strftime("%m/%d")
LOG_FILE_PATH = "./log/"
WORK_STATUS = "-1"

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
        enavi.enavi_reset(WORK_STATUS)
        print("勤怠入力画面\t：OK")
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
