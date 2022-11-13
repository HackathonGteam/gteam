from flask import Flask, request, redirect, render_template, session, flash
from flask_bcrypt import Bcrypt
from models import dbConnect
from datetime import timedelta
import secrets
import uuid
import re


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
    email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    password_pattern = "\A(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{8,32}\Z"

    # フォームで入力された情報の取得
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    # データベースからユーザー名でユーザーを取得
    userByName = dbConnect.getUserByName(name)
    # データベースからメールアドレスでユーザーを取得
    userByEmail = dbConnect.getUserByEmail(email)

    # ユーザー名の妥当性をチェック
    if name == "":
        flash('ユーザー名を入力してください')
    elif userByName != None:
        flash('すでに使用されているユーザー名です')
    else:
        counter -= 1

    # メールアドレスの妥当性をチェック
    if email == "":
        flash('メールアドレスを入力してください')
    elif re.match(email_pattern, email) is None:
        flash('メールアドレスを適切な形式で入力してください')
    elif userByEmail != None:
        flash('すでに使用されているメールアドレスです')
    else:
        counter -= 1

    # パスワードの妥当性をチェック
    if password == "":
        flash('パスワードを入力してください')
    elif re.match(password_pattern, password) is None:
        flash('パスワードは8文字以上32文字以内で、半角英小文字、大文字、数字をそれぞれ1つずつ含めてください')
    else:
        counter -=1

    # パスワード（確認用）の妥当性をチェック
    if confirm_password == "":
        flash('パスワード（確認用）を入力してください')
    elif password != confirm_password:
        flash('パスワードが一致していません')
    else:
        counter -= 1

    # ４項目のチェック項目に合格
    if counter == 0:
        # ユーザーidの生成
        uid = str(uuid.uuid4())
        # パスワードの暗号化
        encryptionPassword = bcrypt.generate_password_hash(password).decode('utf-8')
        # データベースにユーザーを登録
        dbConnect.createUser(uid, name, email, encryptionPassword)
        # セッションの確立
        session['uid'] = uid
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
    elif not bcrypt.check_password_hash(user['password'], password):
        flash('メールアドレスかパスワードが間違っています')
    else:
        # セッションの確立
        session['uid'] = user['uid']
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


#チャネルの作成する


if __name__ == "__main__":
    app.run(port=8080, debug=True)