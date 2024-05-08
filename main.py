import os
from app import create_app

SETTING_NAME = os.environ.get('FLASK_ENV') or 'default'
app = create_app(setting_name=SETTING_NAME)