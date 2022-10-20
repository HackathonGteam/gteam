from flask import Flask, request, redirect, render_template, session
from models import dbConnect
from datetime import timedelta
import secrets
import uuid


app = Flask(__name__)
# セッション情報（クライアントのCookieに保存される）を暗号化する秘密鍵の生成
app.secret_key = secrets.token_hex()
# セッションの寿命を設定
app.permanent_session_lifetime = timedelta(days=30)


# サインアップページにページ遷移
@app.route('/signup')
def signup():
    return render_template('registration/signup.html')


# サインアップ機能
@app.route('/signup', methods=['POST'])
def userSignup():
    # フォームで入力された情報の取得
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    # ユーザーidの生成
    uid = str(uuid.uuid4())

    # データベースの操作
    dbConnect.createUser(uid, name, email, password1)
    # セッションの確立
    session['uid'] = uid

    return redirect('/')


# ログインページにページ遷移
@app.route('/login')
def login():
    return render_template('registration/login.html')


# ログイン機能
@app.route('/login', methods=['POST'])
def userLogin():
    # フォームで入力された情報の取得
    email = request.form.get('email')
    password = request.form.get('password')

    # データベースからユーザーを取得する
    user = dbConnect.getUser(email)

    if user != None and password == user['password']:
        # セッションの確立
        session['uid'] = user['uid']

        return redirect('/')


@app.route('/')
def index():
    return 'Hello World'


if __name__ == "__main__":
    app.run(port=8080, debug=True)