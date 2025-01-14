from main import test
from main.config import APP_VERSION, APP_NAME, APP_WIDTH, APP_HEIGHT


def success(data):
    return {
        "success": True,
        "message": "",
        "data": data
    }


def fail(data, message):
    return {
        "success": False,
        "message": message,
        "data": data
    }


class Api:
    def app_info(self):
        data = {
            "version": APP_VERSION,
            "name": APP_NAME,
            "width": APP_WIDTH,
            "height": APP_HEIGHT,
        }
        return success(data)

    def test(self, params):
        return success(test.test1(params))
