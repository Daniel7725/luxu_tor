#coding:utf-8

import tornado.web
import tornado.ioloop
from tornado.options import define,options #,loggong
from tornado.httpserver import HTTPServer
from app.application import Application

#import os
#import inspect

#app_path = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))

define("port",default=8000,help="run on the given port",type=int)

def main():
    options.parse_command_line()
    app = Application()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    #print app_path
    tornado.ioloop.IOLoop.instance().start()
    print "Quit the server with CONTORL-C"

if __name__ == '__main__':
    main()
