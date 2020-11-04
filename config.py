import os

class Config:
    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY ='3005c01f560af999a1c88e59d059ce'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:sophiecee@localhost/safe-boda'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME ='sophieolondie@gmail.com'
    MAIL_PASSWORD ='whwtyfvhukzsfcgv'
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:sophiecee@localhost/safe-boda'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}