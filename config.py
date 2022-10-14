#!/usr/bin/env python3
# Author: Armit
# Create Time: 2022/10/10

import os

# NOTE: these must be abspath
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
REPO_PATH = os.path.join(BASE_PATH, 'repos')
HTML_PATH = os.path.join(BASE_PATH, 'static', 'html')
CSS_PATH  = os.path.join(BASE_PATH, 'static', 'css')
JS_PATH   = os.path.join(BASE_PATH, 'static', 'js')
FTP_PATH  = os.path.join(BASE_PATH, 'ftp')

DEFAULT_AUTHOR = 'Kahsolt'


os.makedirs(REPO_PATH, exist_ok=True)
os.makedirs(HTML_PATH, exist_ok=True)
os.makedirs(CSS_PATH,  exist_ok=True)
os.makedirs(JS_PATH,   exist_ok=True)
os.makedirs(FTP_PATH,  exist_ok=True)
