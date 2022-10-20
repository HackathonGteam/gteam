import pymysql
from util.DB import DB


class dbConnect:
    def createUser(uid, name, email, password):
      try:
          conn = DB.getConnection()
          cur = conn.cursor()
          sql = "INSERT INTO users (uid, user_name, email, password) VALUES (%s, %s, %s, %s);"
          cur.execute(sql, (uid, name, email, password))
          conn.commit()
      except Exception as e:
          print(e + 'が発生しています')
          return None
      finally:
          cur.close()
          conn.close()