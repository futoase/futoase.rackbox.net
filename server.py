#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import static_file, route, run, default_app
import bottle
bottle.TEMPLATE_PATH.append('./app/views/')

from app.controllers import *
# routes
route('/')(index.main)()

# static file path
@route('/static/<path:path>')
def static(path):
  return static_file(path, './static')

app = default_app()

if __name__ == '__main__':
  import json
  with open('./conf/server.json', 'r') as f:
    setting = json.load(f)

  run(host=setting.get('host'), port=setting.get('port'))
