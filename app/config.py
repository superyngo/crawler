import os
from app.utils.common import *

os.makedirs(STR_DOWNLOADS_TIMESTAMP_FOLDER_PATH, exist_ok=True)

os.environ['HTTPS_PROXY'] = ''
os.environ['HTTP_PROXY'] = ''
