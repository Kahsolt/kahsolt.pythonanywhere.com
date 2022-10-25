#!/usr/bin/env python3
# Author: Armit
# Create Time: 2022/10/14 

import os
import sys
import json
from pprint import pprint
import requests
from argparse import ArgumentParser

sys.path.extend(['.', '..'])
from config import BASE_PATH


with open(os.path.join(BASE_PATH, 'config.json'), encoding='utf-8') as fh:
    config = json.load(fh)['paw']
    USER = config['username']
    TOKEN = config['auth_token']

TOKEN = os.environ.get('TOKEN', TOKEN)       # allow override

HEADERS = { 'Authorization': f'Token {TOKEN}' }
API_BASE = f'https://www.pythonanywhere.com/api/v0/user/{USER}'
DOMAIN_NAME = 'kahsolt.pythonanywhere.com'


def GET(ep):
    res = requests.get(API_BASE + ep, headers=HEADERS)
    if res.status_code == 200:
        return res.json()
    else:
        print(f'Error: {res.status_code} {res.reason}, {res.content}')


def POST(ep, data=None):
    res = requests.post(API_BASE + ep, data=data, headers=HEADERS)
    if res.status_code == 200:
        return res.json()
    else:
        print(f'Error: {res.status_code} {res.reason}, {res.content}')


def api_cpu(args):
    '''
    GET   /api/v0/user/{username}/cpu/
    '''
    
    return GET('/cpu')


def api_consoles(args):
    '''
    GET|POST     /api/v0/user/{username}/consoles/
    GET|DELETE   /api/v0/user/{username}/consoles/{id}/
    POST         /api/v0/user/{username}/consoles/{id}/send_input/
    GET          /api/v0/user/{username}/consoles/{id}/get_latest_output/
    GET          /api/v0/user/{username}/consoles/shared_with_you/
    '''
    return GET('/consoles')


def api_files(args):
    '''
    GET|POST|DELETE   /api/v0/user/{username}/files/path{path}
    GET               /api/v0/user/{username}/files/tree/?path={path}
    POST              /api/v0/user/{username}/files/sharing/
    GET|DELETE        /api/v0/user/{username}/files/sharing/?path={path}
    '''
    return GET('/files/sharing')


def api_webapps(args):
    '''
    GET|POST                /api/v0/user/{username}/webapps/
    GET|PUT|PATCH|DELETE    /api/v0/user/{username}/webapps/{domain_name}/
    POST                    /api/v0/user/{username}/webapps/{domain_name}/enable/
    POST                    /api/v0/user/{username}/webapps/{domain_name}/disable/
    POST                    /api/v0/user/{username}/webapps/{domain_name}/reload/
    GET|POST|DELETE         /api/v0/user/{username}/webapps/{domain_name}/ssl/
    GET|POST                /api/v0/user/{username}/webapps/{domain_name}/static_files/
    GET|PUT|PATCH|DELETE    /api/v0/user/{username}/webapps/{domain_name}/static_files/{id}/
    GET|POST                /api/v0/user/{username}/webapps/{domain_name}/static_headers/
    GET|PUT|PATCH|DELETE    /api/v0/user/{username}/webapps/{domain_name}/static_headers/{id}/
    '''
    return POST(f'/webapps/{DOMAIN_NAME}/reload/')


def api_system_image(args):
    '''
    GET   /api/v0/user/{username}/system_image/
    '''
    return GET('/system_image')


def api_schedule(args):
    '''
    GET|POST               /api/v0/user/{username}/schedule/
    GET|PUT|PATCH|DELETE   /api/v0/user/{username}/schedule/{id}/
    '''
    return GET('/schedule')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-E', '--endpoint', help='endpoint name of API call')
    parser.add_argument('-L', '--list', action='store_true', help='list all endpoints')
    args = parser.parse_args()

    if args.list:
        print('Endpoints:')
        eps = [fn[4:] for fn in globals() if fn.startswith('api_')]
        for ep in eps:
            print(f'   {ep}')
    elif args.endpoint:
        ret = globals().get(f'api_{args.endpoint}')(args)
        pprint(ret)
