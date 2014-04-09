#coding:utf-8
from tornado.web import RequestHandler
import tempfile
#import Image
import time
import logging
import os
import inspect

app_path = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))

try:
    from PIL import Image
except ImportError:
    import Image

class UploadHandler(RequestHandler):
    def post(self):
        image_type_list = ['image/jpeg','image/jpg','image/png']
        if 'mypicture' in self.request.files:
            send_file = self.request.files['mypicture'][0]
        else:
            self.write('donot have the picture')
            return
        if send_file['content_type'] not in image_type_list:
            self.write('不支持图片格式')
            return
        #创建临时文件
        tmp_file = tempfile.NamedTemporaryFile(delete=True)
        tmp_file.write(send_file['body'])
        tmp_file.seek(0)


        try:
            image_one = Image.open(tmp_file.name)
        except IOError,e:
            logging.info(e)
            logging.info('+'*30 + '\n')
            logging.info(self.request.headers)
            tmp_file.close()
            self.write('不合法')
            return

        #进行存储
        try:
            image_path ="./static/picture/"
            image_format = send_file['filename'].split('.').pop().lower()
            tmp_name = image_path + str(int(time.time())) + '.'+image_format
            image_one.save(tmp_name)
        except IOError,e:
            logging.info(e)
            tmp_file.close()
            self.write('hehe')

        tmp_file.close()
        self.write('success'+image_path[1:])
