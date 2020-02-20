# coding:utf8
import logging
import os
import random
import sys

import zxing  # 导入解析包
from PIL import Image
import cv2

logger = logging.getLogger(__name__)  # 记录数据

if not logger.handlers:
    logging.basicConfig(level=logging.INFO)

DEBUG = (logging.getLevelName(logger.getEffectiveLevel()) == 'DEBUG')  # 记录调式过程


# 在当前目录生成临时文件，规避java的路径问题
def ocr_qrcode_zxing(filename):
    img = Image.open(filename)
    ran = int(random.random() * 100000)  # 设置随机数据的大小
    img.save('%s%s.jpg' % (os.path.basename(filename).split('.')[0], ran))
    zx = zxing.BarCodeReader()  # 调用zxing二维码读取包
    data = ''
    zxdata = zx.decode('%s%s.jpg' % (os.path.basename(filename).split('.')[0], ran))  # 图片解码

    # 删除临时文件
    os.remove('%s%s.jpg' % (os.path.basename(filename).split('.')[0], ran))

    if zxdata:
        logger.debug(u'zxing识别二维码:%s,内容: %s' % (filename, zxdata))
        data = zxdata
    else:
        logger.error(u'识别zxing二维码出错:%s' % (filename))
        img.save('%s-zxing.jpg' % filename)
    return data  # 返回记录的内容


def fun(p):
    a = int(p[0])
    b = int(p[1])

    return (a, b)


if __name__ == '__main__':
    filename = str(sys.argv[1])
    #print(sys.argv)
    img = cv2.imread(filename)
    rname = "image/tt.jpg"
    cv2.imwrite(rname, img)
    # zxing二维码识别
    # ltext = ocr_qrcode_zxing(filename)  # 将图片文件里的信息转码放到ltext里面
    # logger.info(u'[%s]Zxing二维码识别:[%s]!!!' % (filename, ltext))  # 记录文本信息
    # print(ltext.raw)  # 打印出二维码名字
    zx = zxing.BarCodeReader()
    date = zx.decode(rname)
    #print(date.points)
    print(date.raw)
    #[p1, p2, p3, p4] = date.points
    #s1 = fun(p1)
    #s2 = fun(p2)
    #s3 = fun(p3)
    #s4 = fun(p4)
    #cv2.line(img, s1, s2, (255, 0, 0), 2)
    #cv2.line(img, s2, s3, (255, 0, 0), 2)
    #cv2.line(img, s3, s4, (255, 0, 0), 2)
    #cv2.line(img, s4, s1, (255, 0, 0), 2)
    #cv2.imshow("aaa", img)
    #cv2.waitKey(5000)
    #print(r_decode(rname))


"""
@API :r_decode(file)
@:param file_name : 图片文件名
@:return : 以字符串形式返回二维码解析结果

"""
def r_decode(file_name):

    image_file = file_name
    img = cv2.imread(image_file)
    temp_name = "temp.jpg"
    cv2.imwrite(temp_name, img)
    zx = zxing.BarCodeReader()
    data = zx.decode(temp_name)
    os.remove(temp_name)
    if data ==None:
        return None
    return data.raw
