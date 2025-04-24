import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://users_owner:npg_Jjy36OlhZPHs@ep-empty-base-a4r182hx-pooler.us-east-1.aws.neon.tech/users?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
