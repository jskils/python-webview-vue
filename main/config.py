# config.py
from dotenv import load_dotenv
import os

load_dotenv()
APP_ENV = os.getenv("APP_ENV", "development")
IS_DEV = True if APP_ENV == 'development' else False

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_NAME = os.getenv("APP_NAME", "python-webview-vue")
APP_WIDTH = 1100
APP_HEIGHT = 700
GUI_ENTRYPOINT = 'http://localhost:5173' if IS_DEV else './gui/index.html'
