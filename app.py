from flask import Flask,session,redirect,render_template,request
from models import dbConnect

#インスタンスの作成→これがないと@app.ところで怒られた
app = Flask(__name__)

#ここはテストをするためだけの無理くりページを表示する行
@app.route('/')
def index():
    return render_template('detail.html')

#メッセージ作成機能
#/messageにアクセスされPOSTメソッドでデータが送信された場合の処理
@app.route('/message',methods=['POST'])
#関数add_messageの定義
def add_message():
	
	#sessionはデータをデータベースに保存することなくデータを取ってくる簡易データベース
	#uidにおそらくuidを格納
    uid=session.get("uid")

	#もしuidが空だったらログインページにリダイレクト
    if uid is None:
        return redirect('/login')

	#messageとchannel_idをリクエスト
    message = request.form.get('message')
    channel_id=request.form.get('channel_id')

    if message:
        dbConnect.createMessage(uid,channel_id,message)

    channel = dbConnect.getChannelById(channel_id)
    messages=dbConnect.getMessageAll(channel_id)

		#取得したhtmlの要素にデータを格納
    return render_template('detail.html',messages=messages,channel=channel,uid=uid)


#メッセージ一覧機能
#/messageにアクセスされた場合の処理
@app.route('/detail/<cid>')
#関数detailの定義
def detail(cid):
	#uidにおそらくuidを格納
	uid=session.get("uid")
	#もしuidが空だったらログインページにリダイレクト
	if uid is None:
			return redirect('/login')
	cid=cid
	
	channel = dbConnect.getChannelById(cid)
	messages=dbConnect.getMessageAll(cid)

	#取得したhtmlの要素にデータを格納
	return render_template('detail.html',messages=messages,channel=channel,uid=uid)


#メッセージ削除機能
#/deletemessageにアクセスされPOSTメソッドでデータが送信された場合の処理
@app.route('/delete_message',methods=['POST'])
#関数delete_messageの定義
def delete_message():
	#uidにおそらくuidを格納
	uid = session.get("uid")
	#もしuidが空だったらログインページにリダイレクト
	if uid is None:
		return redirect('/login')
	#message_idとcidをリクエスト
	message_id=request.form.get('message_id')
	cid=request.form.get('channel_id')
	#message_idを出力
	print(message_id)

	if message_id:
		dbConnect.deleteMessage(message_id)

	
	channel=dbConnect.getChannelById(cid)
	messages=dbConnect.getMessageAll(cid)

	#取得したhtmlの要素にデータを格納
	return render_template('detail.html',messages=messages,channel=channel,uid=uid)

if __name__ == '__main__':
	app.run(debug=True)