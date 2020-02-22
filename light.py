import cv2
import os
import numpy as np

def detected_light(img, box):
    xin, yin, xma, yma = box
    light = img[xin:xma, yin:yma]
    status = []
    l = light.shape
    # w, h = l[0], l[1]
    m = np.mean(np.mean(img, axis=0), axis=0)
    b, g, r = m[0], m[1], m[2]
    if g > b and g > r:
        status = "green"
        if g > 150:
            status += "_on"
        else:
            status += "_off"
    elif r > g and r > b:
        status = "red"
        if r > 150:
            status += "_on"
        else:
            status += "_off"
    else:
        status = "unknow"
    return status


def li_det():
    path = os.listdir("img_light/")
    status=[]
    for p_img in path:
        img = cv2.imread("img_light/" + p_img)
        l = img.shape
        w, h = l[0],l[1]
        m = np.mean(np.mean(img,axis=0),axis=0)
        b, g, r = m[0], m[1], m[2]
        if g>b and g>r:
            status = "green"
            if g >150:
                status += "_on"
            else:
                status += "_off"
        elif r>g and r>b:
            status = "red"
            if r>150:
                status += "_on"
            else:
                status += "_off"
        else:
            status= "unknow"
        print(p_img)
        print(img[int(w/2), int(h/2)])
        print(status)


if __name__ == '__main__':
    li_det()
    # image_path = "/home/liqin/python/relaying/10P1.jpg"
    # img = cv2.imread(image_path)
    # detected_light(img, [3942, 455, 4329, 842])