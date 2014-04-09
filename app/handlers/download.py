#coding:utf-8

from tornado.web import RequestHandler
import os
import logging

home_dir = "/Users/Daniel/Code/me/tor/static"

class DownloadHandler(RequestHandler):
	def get(self,path):
		print path
		img_path = os.path.join(home_dir,path.strip('/'))
		print img_path
		try:
			data = open(img_path,'rb').read()
		except IOError,e:
			logging.info(e)
			self.write("none")
			return
			
		self.set_header('Content-Type','image/jpeg')
		self.set_header('Content-Length',len(data))
		self.write(data)
