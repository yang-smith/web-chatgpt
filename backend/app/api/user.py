from flask import jsonify
from app.models.user import User
from app.api import api_bp

@api_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])
