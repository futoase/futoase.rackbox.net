#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bottle import static_file, route, run
import bottle
bottle.TEMPLATE_PATH.append('./app/views/')

from app.controllers import *
# routes
route('/')(index.main)()

# static file path
@route('/static/<path:path>')
def static(path):
  return static_file(path, './static')

if __name__ == '__main__':
  run(host='localhost', port=9000)
