import os
import shutil
import subprocess

from dotenv import load_dotenv

load_dotenv()
APP_ENV = os.getenv("APP_ENV")
APP_VERSION = os.getenv("APP_VERSION")
APP_NAME = os.getenv("APP_NAME")

# 执行打包
subprocess.run(['pyinstaller', 'build.spec'])

# 压缩
dist_folder = './dist'
zip_folder = f'{APP_NAME}-v{APP_VERSION}'
shutil.make_archive(zip_folder, 'zip', dist_folder)
