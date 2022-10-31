import pymysql
from util.DB import DB

class dbConnect:


    #メッセージ作成機能
    def createMessage(uid,cid,message):
        try:
            conn=DB.getConnection()
            cur=conn.cursor()
            sql="INSERT INTO messages(uid,cid,message) VALUES(%s,%s,%s)"
            cur.execute(sql,(uid,cid,message))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()

    #メッセージ一覧機能
    def getMessageAll(cid):
        try:
            conn=DB.getConnection()
            cur=conn.cursor()
            sql="SELECT id,u,uid,user_name,message,AS m INNER JOIN users AS u ON m.uid=u.uid WHERE cid=%s;"
            cur.execute(sql,(cid))
            messages =cur.fetchall()
            return messages
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()

    #メッセージ削除機能
    def deleteMessage(message_id):
        try:
            conn=DB.getConnection()
            cur=conn.cursor()
            sql="DELETE FROM messages WHERE id=%s;"
            cur.execute(sql,(message_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()