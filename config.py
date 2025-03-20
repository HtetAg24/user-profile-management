import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user_admin:your_password@localhost/user_profile_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
