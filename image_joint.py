import os
import sys


import cv2

from joint.stitch import Stitcher, Method

# os.chdir(os.path.dirname(__file__))
# os.chdir(os.getcwd())
# debug:


def log(*args):
    import logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s:\n %(message)s')
    logging.debug(''.join([str(x) for x in args]))


def read_image(*images):
    res = []
    for i in images[0]:
        res.append(cv2.imread(i))
    return tuple(res)

def read_image_list(image_list):
    res = []
    for i in image_list:
        res.append(cv2.imread(i))
    return tuple(res)

def show_help():
    print("""
用法:
   ～# python main.py  image_path1 image_path2....
-----
    To create stitched image
    """.format(os.path.basename(__file__)))
    exit(1)


def command_api():
    if (len(sys.argv) < 2):
        show_help()

    path_list = sys.argv[1:]

    print(path_list)
    images = read_image(path_list)

    pre_image = []
    pano_image = []
    for index, image in enumerate(images):
        if index == 0:
            pre_image = image
            continue
        s = Stitcher(pre_image, image, Method.ORB, False)
        s.stich()
        pano_image = s.image
        pre_image = pano_image
    save_path = os.getcwd() + "/img/"
    if not (os.path.exists(save_path)):
        os.mkdir(save_path)
    cv2.imwrite(save_path+"pano.jpg", pano_image)
    return save_path + "pano.jpg"

"""
@ API stich_image_api(path_list)
@ ：输入的图片文件个数需大于2及以上 
@:param: path_list like ["../img_pano/q1.jpg", "../img_pano/q2.jpg", "../img_pano/q3.jpg"]
@:return 拼接后图片保存位置
"""

def stich_image_api(path_list,save_path):

    images = read_image_list(path_list)

    pre_image = []
    pano_image = []
    for index, image in enumerate(images):
        if index ==0:
            pre_image = image
            continue
        s = Stitcher(pre_image, image, Method.ORB, False)
        s.stich()
        pano_image = s.image
        pre_image = pano_image
    # save_path = os.getcwd() + "/img_pano/"
    if not (os.path.exists(os.path.dirname(save_path))):
        os.mkdir(os.path.dirname(save_path))
    cv2.imwrite(save_path, pano_image)
    return save_path



def main():
    img_path = command_api()
    # img_path = stich_image_api(["../img_pano/q1.jpg", "../img_pano/q2.jpg", "../img_pano/q3.jpg"])
    print("joint image was saved : ", img_path)

if __name__ == "__main__":

    main()

