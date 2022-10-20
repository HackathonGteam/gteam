from flask import Flask, request, redirect, render_template 
from models import dbConnect
import uuid


app = Flask(__name__)


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
    uid = uuid.uuid4()

    # データベースの操作
    dbConnect.createUser(uid, name, email, password1)
    return redirect('/')


@app.route('/')
def index():
    return 'Hello World'


if __name__ == "__main__":
    app.run(port=8080, debug=True)