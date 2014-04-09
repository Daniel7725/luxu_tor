#coding:utf-8
from handlers import *

urls = [
        # to add urls and handlers
        (r'/',IndexHandler),
        (r'/upload',UploadHandler),
		(r'/download/(.+)',DownloadHandler),
        ]
