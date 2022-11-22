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


    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            #全チャンネルを取得
            sql = "SELECT CHANNEL_ID, U.USER_ID, USER_NAME, CHANNEL_NAME, ABSTRACT FROM CHANNELS AS C INNER JOIN USERS AS U ON C.USER_ID = U.USER_ID ORDER BY CHANNEL_ID DESC;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
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


    def getChannelByName(channelName):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            #チャンネル名からチャンネル名を取得する
            sql = "SELECT * FROM CHANNELS WHERE CHANNEL_NAME=%s;"
            cur.execute(sql, (channelName))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()


    def addChannel(userId, ChannelName, ChannelDescription):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            #チャンネルを登録する
            sql = "INSERT INTO CHANNELS (USER_ID, CHANNEL_NAME, ABSTRACT) VALUES (%s, %s, %s);"
            cur.execute(sql, (userId, ChannelName, ChannelDescription))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()


    def updateChannel(userId, ChannelName, ChannelDescription, channelId):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            #チャンネル情報を更新
            sql = "UPDATE CHANNELS SET USER_ID=%s, CHANNEL_NAME=%s, ABSTRACT=%s WHERE CHANNEL_ID=%s;"
            cur.execute(sql, (userId, ChannelName, ChannelDescription, channelId))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
            conn.close()


    #deleteチャンネル関数
    def deleteChannel(channelId):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            #チャンネルを削除
            sql = "DELETE FROM CHANNELS WHERE CHANNEL_ID=%s;"
            cur.execute(sql, (channelId))
            conn.commit()
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