import os


class Config:
    SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@db:5432/sitesdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('DATABASE_URL', 'postgresql://user:password@db:5432/sitesdb')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_BROKER_URL', 'redis://redis:6379/0')
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    MAIL_USE_TLS = True
