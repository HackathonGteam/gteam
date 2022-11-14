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


    def getUserByName(name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE user_name=%s;"
            cur.execute(sql, (name))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close
            conn.close()


    def getUserByEmail(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close
            conn.close()


    # チャンネルIDでチャンネルを取得
    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()


    # チャンネルIDから全てのメッセージを取得
    def getMessageAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT id, u.uid, user_name, message FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s;"
            cur.execute(sql, (cid))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()


    # メッセージの作成
    def createMessage(uid, cid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
            cur.execute(sql, (uid, cid, message))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()


    # メッセージの削除
    def deleteMessage(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM messages WHERE id=%s;"
            cur.execute(sql, (message_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()