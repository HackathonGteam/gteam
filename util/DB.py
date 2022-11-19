import pymysql

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host="localhost",
            db="MOSSCHAT",
            user="MOSSUSER",
            password="YxADUh64Hf_L",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()