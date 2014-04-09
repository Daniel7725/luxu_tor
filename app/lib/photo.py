#coding:utf-8

"""To upload photos to server.And to download photos to client."""

import tempfile
import time
import logging

try:
    from PIL import Image
except ImportError:
    import Image

IMAGE_WIDTH = 25 #缩略图的默认宽度
IMAGE_TYPE_LIST = ['image/jpeg','image/jpg','image/png']

def upload(load_file,photo_path,header=None):
    """upload photos to server.
    * ``load_file``:post表单调用request.files[]的返回值.
    * ``photo_path``:photo在服务器上存储的路径.
    * ``header``:http请求的表头
    """

    if load_file['content_type'] not in IMAGE_TYPE_LIST:
        return -1 #表示不支持的图片格式
    #创建临时文件
    tmp_file = tempfile.NamedTemporaryFile(delete=True) #关闭之后，删除
    tmp_file.write(load_file['body'])
    tmp_file.seek(0) #读取完之后，指针处于末尾，需要重新指向头部

    try:
        image_one = Image.open(tmp_file.name)
    except IOError,e:
        logging.info(e)
        logging.info('+'*30 + '\n')
        logging.info(header)
        tmp_file.close()
        return -2 #表示图片实质的格式存在欺诈！用日志记录，防止恶意攻击.

    #进行原始图片和缩略图的存储
    try:
        image_format = load_file['filename'].split('.').pop().lower()
        tmp_name = str(int(time.time())) + '.' +image_format #图片名称
        tmp_small_name = photo_path+'small/'+tmp_name #缩略图的路径+名称
        tmp_photo_name = photo_path+tmp_name #原始图片的路径+名称

        image_small_one = photo_small(image_one,IMAGE_WIDTH)
        image_small_one.save(tmp_small_name)  #存储缩略图

        image_one.save(tmp_photo_name)  #存储原始图片
    except IOError,e:
        logging.info(e)
        tmp_file.close()
        return 0 #表示存储失败

    tmp_file.close()
    return tmp_small_name #返回路径和文件名，表示存储成功

def photo_small(img,img_width):
    """将图片按照给定的宽进行等比例缩小.
    * ``img``:图片流.
    * ``img_width``:图片的宽度.
    返回照片流.
    """

    img_width = int(img_width)
    tmp_width,tmp_high = img.size
    img_high = img_width*(float(tmp_high)/float(tmp_width))
    return img.resize((int(img_width),int(img_high)),Image.ANTIALIAS)
