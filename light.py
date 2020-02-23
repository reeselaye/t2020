import cv2
import os
import numpy as np
import time

def detected_light(img, box):
    xin, yin, xma, yma = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    light = img[yin:yma, xin:xma]
    status = []
    l = light.shape
    w, h = l[0], l[1]
    m = np.mean(np.mean(light, axis=0), axis=0)
    b, g, r = m[0], m[1], m[2]
    if g > b and g > r:
        status = "green"
        if g > 150 and g > r + 30:
            status += "_on"
        else:
            status += "_off"
    elif r > g and r > b:
        status = "red"
        if r > 150 and r > g + 30:
            status += "_on"
        else:
            status += "_off"
    elif g > r:
        status = "green"
        if g > 150 and g > r + 30:
            status += "_on"
        else:
            status += "_off"
    elif r > g:
        status = "red"
        if r > 150 and r > g + 30:
            status += "_on"
        else:
            status += "_off"
    else:
        status = "unknow"
    # cv2.imwrite("img_light/"+ str(time.time())+".jpg", light)
    # print("---", status)
    # print(light[int(w / 2), int(h / 2)])
    # print(b, "-", g, "-", r)
    return status


def li_det():
    path = os.listdir("img_light/")
    status=[]
    for p_img in path:
        img = cv2.imread("img_light/" + p_img)
        l = img.shape
        w, h = l[0],l[1]
        # b = img[int(w/2),int(h/2)][0]
        # g = img[int(w/2), int(h/2)][1]
        # r = img[int(w/2), int(h/2)][2]
        m = np.mean(np.mean(img,axis=0),axis=0)
        b, g, r = m[0], m[1], m[2]
        if g>b and g>r:
            status = "green"
            if g >150 and g>r+30:
                status += "_on"
            else:
                status += "_off"
        elif r>g and r>b:
            status = "red"
            if r>150 and r>g+30:
                status += "_on"
            else:
                status += "_off"
        elif g>r:
            status= "green"
            if g >150 and g>r+30:
                status += "_on"
            else:
                status += "_off"
        elif r>g:
            status = "red"
            if r>150 and r>g+30:
                status += "_on"
            else:
                status += "_off"

        print(p_img,"---",status)
        print(img[int(w/2), int(h/2)])
        print(b, "-", g, "-", r)
        # print(status)


if __name__ == '__main__':
    li_det()
    # image_path = "/home/liqin/python/relaying/10P1.jpg"
    # img = cv2.imread(image_path)
    # detected_light(img, [3942, 455, 4329, 842])
