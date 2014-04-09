#coding:utf-8

from urls import urls
import os

import tornado.web


class Application(tornado.web.Application):
    def __init__(self):

        handlers = urls
        settings = dict(
                #To add settings about this program.
                template_path = os.path.join(os.path.dirname(__file__),"view"),
                debug=True
                )
        tornado.web.Application.__init__(self,handlers,**settings)
