import tornado.ioloop
import tornado.web
import tornado.httpserver
import sqlite3
import os
import json,time
from hashlib import md5
import random
import router

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "html"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    login_url= "/login"
)
application = tornado.web.Application(router.Router,**settings)
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(8080)
print("Begin to receive　Request!")
tornado.ioloop.IOLoop.instance().start()