from flask import request, jsonify, make_response
from app import db
from app.models.user import User
from app.utils.token import generate_token
from app.api import api_bp

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user is not None and user.check_password(password):
        token = generate_token(user)
        return jsonify({"token": token})
    else:
        return make_response(jsonify({"error": "Invalid username or password"}), 401)
