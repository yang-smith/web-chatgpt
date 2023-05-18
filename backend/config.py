import os
from dotenv import load_dotenv

class Config:
    # 加载.env文件
    load_dotenv()

    # 从.env文件中读取数据库连接信息和API密钥
    db_connection = os.environ.get("DB_CONNECTION")
    api_key = os.environ.get("API_KEY")
    
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_CONNECTION")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
