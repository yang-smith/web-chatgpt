import jwt
from flask import current_app
from app.models.user import User
import time

def generate_token(user, expires_in=86400):
    payload = {
        'user_id': user.id,
        'exp': time.time() + expires_in
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, current_app
        .config['SECRET_KEY'], algorithms=['HS256'])
        return User.query.get(payload['user_id'])
    except jwt.exceptions.ExpiredSignatureError:
        return None
    except jwt.exceptions.InvalidTokenError:
        return None

def validate_token(token):
    try:
        payload = jwt.decode(token, current_app
        .config['SECRET_KEY'], algorithms=['HS256'])
        return payload
    except jwt.exceptions.ExpiredSignatureError:
        return None
    except jwt.exceptions.InvalidTokenError:
        return None
