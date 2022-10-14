#!/usr/bin/env python3
# Author: Armit
# Create Time: 2022/10/10 

import os
import sys
import builtins
import traceback 
import shutil as sh
from typing import List, Tuple

sys.path.extend(['.', '..'])
from config import *


def run(cmd:str, echo=True):
  print(f'[exec] {cmd}')
  r = os.popen(cmd).read().strip()
  if echo and r: print(r)
  return r


def prepare_repo(repo_name:str, author:str=DEFAULT_AUTHOR) -> str:
  repo_dp = os.path.join(REPO_PATH, repo_name)
  if os.path.exists(repo_dp):
    git_pull(repo_name)
  else:
    git_clone(repo_name, author)
    repo_dp = os.path.join(REPO_PATH, repo_name)
  return repo_dp


def chdir(fn):
  def wrapper(*args, **kwargs):
    saved_dp = os.getcwd()
    os.chdir(REPO_PATH)
    r = fn(*args, **kwargs)
    os.chdir(saved_dp)
    return r
  return wrapper


@chdir
def git_clone(repo_name:str, author:str=DEFAULT_AUTHOR):
  url = f'https://github.com/{author}/{repo_name}.git'
  
  try:
    run(f'git clone {url}')
  except Exception:
    traceback.print_exc()
    exit(-1)


@chdir
def git_pull(repo_name:str):
  save_dp = os.getcwd()
  os.chdir(repo_name)

  try:
    run('git reset')
    run('git pull')
  except Exception:
    traceback.print_exc()
    exit(-1)

  os.chdir(save_dp)


def robocopy(src:str, dst:str, sess_opt:str=None) -> str:
  if not os.path.exists(src):
    raise ValueError(f'[robocopy] src {src} not exists!')

  if os.path.isfile(src) and os.path.isdir(dst):
    dst = os.path.join(dst, os.path.basename(src))
  
  if not os.path.exists(dst):
    print(f'[robocopy] copy {src} to {dst}')
    if os.path.isfile(src):
      sh.copy(src, dst)
    else:
      sh.copytree(src, dst)
  else:
    opt = sess_opt
    if not opt:               # ask for action if opt is None
      print(f'[robocopy] dst {dst!r} already exists, overwrite?')
      while opt not in ['y', 'n', 'a', 'yes', 'no', 'abort', 'ya', 'na']:
        print(f'>> [Y] yes / [N] no / [YA] yes to all / [NA] no to all / [A] abort: ', end='')
        opt = input().lower()

    if opt in ['ya', 'na']:   # only these opts are session-wise
      sess_opt = opt

    if opt in ['y', 'yes', 'ya']:
      print(f'[robocopy] copy {src} to {dst}')
      if os.path.isfile(dst):
        os.unlink(dst)
        sh.copy(src, dst)
      else:
        sh.rmtree(dst)
        sh.copytree(src, dst)
    elif opt in ['n', 'no', 'na']:
      print(f'[robocopy] ignore {src}')
    elif opt in ['a', 'abort']:
      print('[robocopy] abort!')
      exit(-1)
    else: raise

  return sess_opt


def install(plan:List[Tuple[str, str]]):
  sess_opt = None   # interactive choice within session
  for src, dst in plan:
    sess_opt = robocopy(src, dst, sess_opt)


def open_with_utf8(fp, mode='r', *args, **kwargs):
  if 'b' in mode:
    return _open(fp, mode, *args, **kwargs)
  else:
    return _open(fp, mode, encoding='utf-8', *args, **kwargs)

_open = builtins.open
open = open_with_utf8
