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
            

    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            #全チャンネルを取得
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()

        # チャンネルIDでチャンネルを取得
    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            #IDからチャンネルを取得
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            #チャンネル名からチャンネル名を取得する
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def addChannel(uid, newChannelName, newChannelDescription):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            #チャンネルを登録する
            sql = "INSERT INTO channels (uid, name, abstract) VALUES (%s, %s, %s);"
            cur.execute(sql, (uid, newChannelName, newChannelDescription))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            #チャンネル名からチャンネル情報を取得
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
        except Exception as e:
            print(e + 'が発生しました')
            return None
        finally:
            cur.close()
            return channel


    def updateChannel(uid, newChannelName, newChannelDescription, cid):
        conn = DB.getConnection()
        cur = conn.cursor()
        #チャンネル情報を更新
        sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
        cur.execute(sql, (uid, newChannelName, newChannelDescription, cid))
        conn.commit()
        cur.close()


    #deleteチャンネル関数
    def deleteChannel(cid):
        try: 
            conn = DB.getConnection()
            cur = conn.cursor()
            #チャンネルを削除
            sql = "DELETE FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()