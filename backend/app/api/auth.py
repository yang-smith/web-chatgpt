from flask import request, jsonify, make_response
from app import db
from app.models.user import User
from app.utils.token import generate_token, validate_token
from app.api import api_bp

@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    initial_balance = data.get('balance', 0.0)  

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

    user = User(username=username, email=email, balance=initial_balance)  
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
        return jsonify({"token": token, "balance": user.balance, "message": "登录成功！"}), 200  
    else:
        return make_response(jsonify({"error": "无效的电子邮件或密码"}), 401)


@api_bp.route('/update_balance', methods=['POST'])
def update_balance():
    # 这个API需要一个合法的用户Token和新的余额值
    data = request.get_json()
    token = data.get('token')
    new_balance = data.get('new_balance')

    if token is None or new_balance is None:
        return make_response(
            jsonify({"error": "Token and new balance are required"}), 400
        )

    # 验证Token的有效性，并获取用户信息
    user_info = validate_token(token)
    if user_info is None:
        return make_response(
            jsonify({"error": "Invalid token"}), 403
        )

    # 查询用户，并更新余额
    user = User.query.get(user_info['user_id'])
    if user is None:
        return make_response(
            jsonify({"error": "User not found"}), 404
        )

    user.balance = new_balance
    db.session.commit()

    return jsonify({"message": "Balance updated successfully"}), 200

