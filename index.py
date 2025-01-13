import logging
import webview

from src.config import *
from src.api import Api

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf8'),
        logging.StreamHandler()
    ]
)

if __name__ == '__main__':
    webview.create_window(
        f'{APP_NAME} {APP_VERSION}',
        GUI_ENTRYPOINT,
        js_api=Api(),
        width=APP_WIDTH,
        height=APP_HEIGHT)
    webview.start(debug=IS_DEV)
