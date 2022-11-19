import pymysql
from util.DB import DB


class dbConnect:
    def createUser(userId, userName, email, password):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO USERS (USER_ID, USER_NAME, EMAIL, PASSWORD) VALUES (%s, %s, %s, %s);"
            cur.execute(sql, (userId, userName, email, password))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()


    def getUserByUserName(userName):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM USERS WHERE USER_NAME=%s;"
            cur.execute(sql, (userName))
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
            sql = "SELECT * FROM USERS WHERE EMAIL=%s;"
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
    def getChannelById(channelId):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM CHANNELS WHERE CHANNEL_ID=%s;"
            cur.execute(sql, (channelId))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()


    # チャンネルIDから全てのメッセージを取得
    def getMessageAll(channelId):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT MESSAGE_ID, U.USER_ID, USER_NAME, MESSAGE FROM MESSAGES AS M INNER JOIN USERS AS U ON M.USER_ID = U.USER_ID WHERE CHANNEL_ID = %s;"
            cur.execute(sql, (channelId))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()


    # メッセージの作成
    def createMessage(userId, channelId, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO MESSAGES(USER_ID, CHANNEL_ID, MESSAGE) VALUES(%s, %s, %s)"
            cur.execute(sql, (userId, channelId, message))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()


    # メッセージの削除
    def deleteMessage(messageId):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM MESSAGES WHERE MESSAGE_ID=%s;"
            cur.execute(sql, (messageId))
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