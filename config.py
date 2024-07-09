import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3307/company'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')