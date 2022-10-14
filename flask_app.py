#!/usr/bin/env python3
# Author: Armit
# Create Time: 2022/09/24
# Update Time: 2022/10/10

import os

from flask import Flask
from flask import redirect, abort

from config import *
from modules import ngrok_stat as ngrok


app = Flask(__name__)


@app.route('/')
def index():
  with open(os.path.join(BASE_PATH, 'index.html'), 'r', encoding='utf-8') as fh:
    return fh.read().strip()


@app.route('/a-puzzle-a-day-ext')
def a_puzzle_a_day_ext():
  with open(os.path.join(HTML_PATH, 'a-puzzle-a-day-ext.html'), 'r', encoding='utf-8') as fh:
    return fh.read().strip()


@app.route('/stable-diffusion-webui-lite')
def stable_diffusion_webui_lite():
  return redirect('/ngrok/site')


@app.route('/ngrok/site')
def ngrok_site():
  ngrok.update_ngrok_info()

  public_urls = ngrok.get_ngrok_public_urls()
  if len(public_urls) == 0:
    return '<p> No ngrok public tunnels found, check the status info: <a href="/ngrok/status">Ngrok Debug</a> </p>'
  elif len(public_urls) == 1:
    return redirect(public_urls[0])
  else:
    return '<ul>{}</ul>'.format('\n'.join([f'<li><a href="{url}">{url}</a></li>' for url in public_urls]))

@app.route('/ngrok/status')
def ngrok_status():
  html = '<div><a href="/ngrok/refresh">Force Refresh State!!</a></div>\n'
  html += ngrok.format_ngrok_info_html()
  return html

@app.route('/ngrok/refresh')
def ngrok_refresh():
  ngrok.update_ngrok_info(hayaku=True)
  return redirect('/ngrok/status')


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
