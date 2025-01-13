# config.py

IS_DEV = True

APP_NAME = "Python Webview Vue"
APP_VERSION = "1.0.0"
APP_WIDTH = 1100
APP_HEIGHT = 700
GUI_ENTRYPOINT = 'http://localhost:5173' if IS_DEV else './gui/index.html'
