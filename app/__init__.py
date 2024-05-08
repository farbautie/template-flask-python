from flask import Flask
from settings import settings

def create_app(setting_name):
    app = Flask(__name__)
    app.config.from_object(settings[setting_name])
    
    settings[setting_name].init_app(app)
    
    return app

