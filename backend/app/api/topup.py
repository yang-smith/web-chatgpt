from flask import request, jsonify, make_response
from app import db
from app.models.user import User
from app.models.topup_record import TopUpRecord
from app.utils.token import generate_token, validate_token
from app.api import api_bp

@api_bp.route('/top_up', methods=['POST'])
def top_up():
    # 这个API需要一个合法的用户Token和充值金额
    data = request.get_json()
    token = data.get('token')
    topup_amount = data.get('amount')

    if token is None or topup_amount is None:
        return make_response(
            jsonify({"error": "Token and topup amount are required"}), 400
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

    # 创建充值记录
    topup_record = TopUpRecord(amount=topup_amount, user_id=user.id)
    db.session.add(topup_record)
    
    user.balance += topup_amount
    db.session.commit()

    return jsonify({"message": "Top up successfully"}), 200
