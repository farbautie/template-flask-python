import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

class Settings(object):
    
    @staticmethod
    def init_app(app: Flask):
        pass
    
class DevelopmentSettings(Settings):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')

class ProductionSettings(Settings):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''


class TestingSettings(Settings):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'
        
        
settings = {
    'development': DevelopmentSettings,
    'prodction': ProductionSettings,
    'testing': TestingSettings,
    'default': DevelopmentSettings
}