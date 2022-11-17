import re
import secrets
import uuid
from datetime import timedelta

from flask import Flask, flash, redirect, render_template, request, session
from flask_bcrypt import Bcrypt

from models import dbConnect

app = Flask(__name__)
bcrypt = Bcrypt(app)
# セッション情報（クライアントのCookieに保存される）を暗号化する秘密鍵の生成
app.secret_key = secrets.token_hex()
# セッションの寿命を設定
app.permanent_session_lifetime = timedelta(days=30)


# サインアップページにページ遷移
@app.route('/signup')
def signup():
    return render_template('signup.html')


# サインアップ機能
@app.route('/signup', methods=['POST'])
def userSignup():
    # カウンタ（フォームで入力された４項目の妥当性をチェックする）
    counter = 4
    # 正規表現
    emailPattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    passwordPattern = "\A(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{8,32}\Z"

    # フォームで入力された情報の取得
    userName = request.form.get('userName')
    email = request.form.get('email')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')

    # データベースからユーザー名でユーザーを取得
    userByUserName = dbConnect.getUserByUserName(userName)
    # データベースからメールアドレスでユーザーを取得
    userByEmail = dbConnect.getUserByEmail(email)

    # ユーザー名の妥当性をチェック
    if userName == "":
        flash('ユーザー名を入力してください')
    elif userByUserName != None:
        flash('すでに使用されているユーザー名です')
    else:
        counter -= 1

    # メールアドレスの妥当性をチェック
    if email == "":
        flash('メールアドレスを入力してください')
    elif re.match(emailPattern, email) is None:
        flash('メールアドレスを適切な形式で入力してください')
    elif userByEmail != None:
        flash('すでに使用されているメールアドレスです')
    else:
        counter -= 1

    # パスワードの妥当性をチェック
    if password == "":
        flash('パスワードを入力してください')
    elif re.match(passwordPattern, password) is None:
        flash('パスワードは8文字以上32文字以内で、半角英小文字、大文字、数字をそれぞれ1つずつ含めてください')
    else:
        counter -=1

    # パスワード（確認用）の妥当性をチェック
    if confirmPassword == "":
        flash('パスワード（確認用）を入力してください')
    elif password != confirmPassword:
        flash('パスワードが一致していません')
    else:
        counter -= 1

    # ４項目のチェック項目に合格
    if counter == 0:
        # ユーザーidの生成
        userId = str(uuid.uuid4())
        # パスワードの暗号化
        encryptionPassword = bcrypt.generate_password_hash(password).decode('utf-8')
        # データベースにユーザーを登録
        dbConnect.createUser(userId, userName, email, encryptionPassword)
        # セッションの確立
        session['userId'] = userId
        return redirect('/')

    return redirect('/signup')


# ログインページにページ遷移
@app.route('/login')
def login():
    return render_template('login.html')


# ログイン機能
@app.route('/login', methods=['POST'])
def userLogin():
    # フォームで入力された情報の取得
    email = request.form.get('email')
    password = request.form.get('password')

    # データベースからメールアドレスでユーザーを取得
    user = dbConnect.getUserByEmail(email)

    if email == "" or password == "":
        if email == "":
            flash('メールアドレスを入力してください')
        if password == "":
            flash('パスワードを入力してください')
    elif user is None:
        flash('メールアドレスかパスワードが間違っています')
    elif not bcrypt.check_password_hash(user['PASSWORD'], password):
        flash('メールアドレスかパスワードが間違っています')
    else:
        # セッションの確立
        session['userId'] = user['USER_ID']
        return redirect('/')

    return redirect('/login')


# ログアウト機能
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/')
def index():
    return 'Hello World'


# メッセージ一覧機能
@app.route('/detail/<channelId>')
def detail(channelId):
    userId = session.get('userId')
    # もしuidが空だったらログインページにリダイレクト
    if userId is None:
        return redirect('/login')

    channelId = channelId
    # データベースからチャンネルを取得する
    channel = dbConnect.getChannelById(channelId)
    # データベースから全てのメッセージを取得する
    messages = dbConnect.getMessageAll(channelId)

    return render_template('detail.html', messages=messages, channel=channel, userId=userId)


# メッセージ作成機能
# /messageにアクセスされPOSTメソッドでデータが送信された場合の処理
@app.route('/message', methods=['POST'])
def add_message():
    userId = session.get('userId')
    # もしuidが空だったらログインページにリダイレクト
    if userId is None:
        return redirect('/login')

    # messageとchannel_idをリクエスト
    message = request.form.get('message')
    channelId = request.form.get('channelId')

    # 入力されたメッセージが空でなければデータベースを操作しメッセージを作成する
    if message:
        dbConnect.createMessage(userId, channelId, message)

    # データベースからチャンネルを取得する
    channel = dbConnect.getChannelById(channelId)
    # データベースから全てのメッセージを取得する
    messages = dbConnect.getMessageAll(channelId)

    return render_template('detail.html', messages=messages, channel=channel, userId=userId)


# メッセージ削除機能
# /deletemessageにアクセスされPOSTメソッドでデータが送信された場合の処理
@app.route('/delete_message', methods=['POST'])
def delete_message():
    userId = session.get('userId')
    #もしuidが空だったらログインページにリダイレクト
    if userId is None:
        return redirect('/login')

    # message_idとchannel_idをリクエスト
    messageId = request.form.get('messageId')
    channelId = request.form.get('channelId')

    if messageId:
        dbConnect.deleteMessage(messageId)

    # データベースからチャンネルを取得する
    channel = dbConnect.getChannelById(channelId)
    # データベースから全てのメッセージを取得する
    messages = dbConnect.getMessageAll(channelId)

    return render_template('detail.html', messages=messages, channel=channel, userId=userId)


#チャネルの作成する


if __name__ == "__main__":
    app.run(port=8080, debug=True)