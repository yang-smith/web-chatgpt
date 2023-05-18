from flask import request, jsonify, make_response
from app import db
from app.models.user import User
from app.utils.token import generate_token
from app.api import api_bp

@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if username is None or email is None or password is None:
        return make_response(
            jsonify({"error": "Username, email, and password are required"}), 400
        )

    if User.query.filter_by(username=username).first() is not None:
        return make_response(
            jsonify({"error": "Username already exists"}), 400
        )

    if User.query.filter_by(email=email).first() is not None:
        return make_response(
            jsonify({"error": "Email already exists"}), 400
        )

    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user is not None and user.check_password(password):
        token = generate_token(user)
        return jsonify({"token": token, "message": "登录成功！"}), 200
    else:
        return make_response(jsonify({"error": "无效的电子邮件或密码"}), 401)

