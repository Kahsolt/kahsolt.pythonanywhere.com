#!/usr/bin/env python3
# Author: Armit
# Create Time: 2022/10/10 

from util import *

REPO_NAME = ''


def deploy():
  print('>> download...')
  repo_dp = prepare_repo(REPO_NAME)

  print('>> deploy...')

  # install plan
  os.chdir(repo_dp)
  install([
    ('w3.css', CSS_PATH),
    ('solver.js', JS_PATH),
    ('index.html', os.path.join(HTML_PATH, f'{REPO_NAME}.html')),
  ])


if __name__ == '__main__':
  deploy()
