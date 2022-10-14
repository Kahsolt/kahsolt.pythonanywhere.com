#!/usr/bin/env python3
# Author: Armit
# Create Time: 2022/09/24
# Update Time: 2022/10/10

import os
import traceback

from flask import Flask
from flask import redirect, abort

from config import *

app = Flask(__name__)


@app.route('/')
def index():
  with open(os.path.join(BASE_PATH, 'index.html'), 'r', encoding='utf-8') as fh:
    return fh.read().strip()


@app.route('/stable-diffusion-webui-lite')
def stable_diffusion_webui_lite():
    return redirect('https://985a-183-192-109-11.jp.ngrok.io')


@app.route('/a-puzzle-a-day-ext')
def a_puzzle_a_day_ext():
  try:
    with open(os.path.join(HTML_PATH, 'a-puzzle-a-day-ext.html'), 'r', encoding='utf-8') as fh:
      return fh.read().strip()
  except:
    return traceback.format_exc()


@app.route('/debug')
def debug():
  s = ''
  s += f'<p>os.getcwd(): {os.getcwd()}</p>'
  s += f'<p>BASE_PATH: {BASE_PATH}</p>'
  s += f'<p>REPO_PATH: {REPO_PATH}</p>'
  s += f'<p>HTML_PATH: {HTML_PATH}</p>'
  s += f'<p>CSS_PATH: {CSS_PATH}</p>'
  s += f'<p>JS_PATH: {JS_PATH}</p>'
  s += f'<p>FTP_PATH: {FTP_PATH}</p>'
  s += f'<p>DEFAULT_AUTHOR: {DEFAULT_AUTHOR}</p>'
  return s
