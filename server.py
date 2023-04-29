from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

import openai
from flask_cors import CORS
from dotenv import load_dotenv
import os



app = Flask(__name__)
CORS(app)  # 添加这一行以允许跨域请求

# 加载.env文件
load_dotenv()

# 从.env文件中读取数据库连接信息和API密钥
db_connection = os.environ.get("DB_CONNECTION")
api_key = os.environ.get("API_KEY")

openai.api_key = api_key
# 替换为您的数据库连接信息
app.config["SQLALCHEMY_DATABASE_URI"] = db_connection
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()
        if existing_user is None:
            user = User(username=username, email=email, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login"))
        else:
            return "User already exists. Please log in."

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = request.form.get("remember")

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user, remember=remember)
            return redirect(url_for("chart"))
        else:
            return "Invalid email or password."

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/api/chart", methods=["GET"])
@login_required
def chart():
    try:
        content = request.args.get("content", "")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": content}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.7,
        )
        message = response['choices'][0]['message']['content']
        return jsonify(message=message)
    except Exception as err:
        return jsonify(error=str(err)), 404


@app.route("/api/chartBeta", methods=["GET"])
def chartBeta():
    try:
        content = request.args.get("content", "")
        response = openai.ChatCompletion.create(
            model="gpt-4-0314",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": content}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.7,
        )
        message = response['choices'][0]['message']['content']
        return jsonify(message=message)
    except Exception as err:
        return jsonify(error=str(err)), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1200)
