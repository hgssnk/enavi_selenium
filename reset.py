# -*- coding: utf-8 -*-

import ENavi

# 定数
URL = "https://hogehoge"
USER_ID = "9999"
USER_PASSWORD = "9999"
DATE = "01/09"
WORK_STATUS = "20"
LOG_FILE_PATH = "./"

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
        enavi.enavi_reset(WORK_STATUS, LOG_FILE_PATH)
        print("勤怠入力画面\t：OK")
        print("TOTAL\t\t：正常終了")
    # 例外処理
    except Exception as e:
        print("こけた")
        print(e)
    # 終了処理
    finally:
        enavi.enavi_end()

if __name__ == "__main__":
    main()
