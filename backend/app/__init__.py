from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)  # 添加这一行以允许跨域请求
    app.config.from_object(config_class)

    db.init_app(app)

    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
