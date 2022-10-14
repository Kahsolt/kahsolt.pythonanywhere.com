#!/usr/bin/env python3
# Author: Armit
# Create Time: 2022/10/10 

from util import *

REPO_NAME = 'a-puzzle-a-day-ext'


def deploy():
  print('>> download...')
  repo_dp = prepare_repo(REPO_NAME)

  print('>> deploy...')

  # install plan
  os.chdir(repo_dp)
  dst_fp = os.path.join(HTML_PATH, f'{REPO_NAME}.html')
  install([
    ('w3.css', CSS_PATH),
    ('solver.js', JS_PATH),
    ('index.html', dst_fp),
  ])

  # update links to js/css
  with open(dst_fp, 'r') as fh: html = fh.read()
  html = html.replace('src="solver.js"', 'src="/static/js/solver.js"', 1)
  html = html.replace('href="w3.css"', 'href="/static/css/w3.css"', 1)
  with open(dst_fp, 'w') as fh: fh.write(html)

  print('>> done!')

if __name__ == '__main__':
  deploy()
