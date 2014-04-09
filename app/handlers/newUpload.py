#coding:utf-8
from tornado.web import RequestHandler
from ..lib.photo import upload


class UploadHandler(RequestHandler):
    def post(self):
        if 'mypicture' in self.request.files:
            send_file = self.request.files['mypicture'][0]
        else:
            self.write('donot hava the picture')
            
        image_path = './static/picture/'

        tmp = upload(send_file,image_path,self.request.headers)
        if isinstance(tmp,int):
            if tmp == -1:
                self.write("格式不支持")
            else:
                self.write("图片欺诈")
        else:
            self.write(tmp)
