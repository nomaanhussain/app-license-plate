import os


class Config(object):
    ENV = 'local'
    DEBUG = True

    SECRET_KEY = b'\x82\x92\xbc\xc2\xcc\x99\xf6\x93\xc9\xd5 \x80\x06\x1c\x8c\x11'
    
    SQLALCHEMY_DATABASE_URI = f""

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False


