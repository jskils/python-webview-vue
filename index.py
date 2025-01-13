import logging
import os

import webview

from config import *
from api.api import Api


def setup_logging():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO,
                        filename=os.path.join('log/app.log'),
                        encoding='utf8')
    logger = logging.getLogger()
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


if __name__ == '__main__':
    setup_logging()
    webview.create_window(
        f'{APP_NAME} {APP_VERSION}',
        GUI_ENTRYPOINT,
        js_api=Api(),
        width=APP_WIDTH,
        height=APP_HEIGHT)
    webview.start(debug=IS_DEV)
