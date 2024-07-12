import logging
import os
import webview

from script import test


def setup_logging():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO,
                        filename=os.path.join('app.log'),
                        encoding='utf8')
    logger = logging.getLogger()
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


class Api:
    def test(self, params):
        return test.test1(params)


def get_entrypoint():
    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if exists('../Resources/gui/index.html'):
        return '../Resources/gui/index.html'

    if exists('./gui/index.html'):
        return './gui/index.html'

    return 'http://localhost:5173'


if __name__ == '__main__':
    setup_logging()
    window = webview.create_window('Python Webview Vue', get_entrypoint(), js_api=Api(), width=1100, height=700)
    webview.start(debug=False)
