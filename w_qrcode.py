# coding:utf8
import os
import sys
import time

import qrcode
  # 临时存储位置

data = input("输入 :")  # 运行时输入数据

QRImagePath = os.getcwd()+"/image/"+data+".png"

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    version=1,
    box_size=10,
    border=2,
)  #
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()
print(QRImagePath)
img.save(QRImagePath)  # 生成图片

if sys.platform.find('darwin') >= 0:
    os.system('open %s' % QRImagePath)

elif sys.platform.find('linux') >= 0:
    os.system('xdg-open %s' % QRImagePath)
else:
    os.system('call %s' % QRImagePath)

time.sleep(5)  # 间隔5个单位
# os.remove(QRImagePath)  # 删除图片
