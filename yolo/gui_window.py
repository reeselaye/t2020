#!/usr/bin/env python
# !encoding:utf-8
# !filename:test_filedialog.py
import tkinter.filedialog as filedialog
from tkinter import *
import os
from tkinter import *
import image_demo
import cv2
import numpy as np


def covt_box_matrix(bboxes):
    # bboxes
    # [xmin,ymin,xmax,ymax]
    # sort_box = sorted(bboxes, key = lambda x: x[1])
    # text_matrix=[]
    # lis=[]
    box = bboxes
    for idx, item1 in enumerate(bboxes):
        #     # text_matrix.append([jj[0],int(jj[5])])
        #     if idx==0:
        #         a=item
        #         b=[]

        if idx == 0: continue
        for idx2, item2 in enumerate(bboxes):

            if np.abs(item1[1] - item2[1]) < item2[3] - item2[1]:
                box[idx2][1] = item1[1]

            # else:
            #     a = item
            #     b.append(item)

        # text_matrix.append(int(item[5]))
        # if idx>1 and sort_box[idx][1] < sort_box[idx-1][1]+500:
        #     lis.append(text_matrix)
        #     text_matrix = []
    sort_box = sorted(box, key=lambda x: (x[1], x[0]))

    # sequence_box.append(jj[0])
    a = []
    text_matrix=[]
    for id, item in enumerate(sort_box):
        a.append(int(item[5]))
        if id<len(sort_box)-1 and sort_box[id+1][0]<item[0]:
            text_matrix.append(a)
            a=[]
    text_matrix.append(a)
    print len(text_matrix)
    return text_matrix
    # pass


def callback(i=0):
    # global i
    # entry.delete(0, END)  # 清空entry里面的内容
    # listbox_filename.delete(0, END)
    # 调用filedialog模块的askdirectory()函数去打开文件夹
    global filepath
    # filepath = filedialog.askdirectory()
    cur = filedialog.askopenfilenames(
        filetypes=[('pic files', ('.jpg', '.png', '.jpeg')), ('pythonfiles', ('.py', '.pyw', '.*'))])
    print cur[0]
    entry.delete(0, END)
    entry.insert(0, cur)
    listbox_filename.insert(i, ' ')
    # i += 2
    listbox_filename.insert(i, 'filename: ' + cur[0])
    i += 1
    listbox_filename.insert(i, 'detected output: ')
    image, bboxes = image_demo.image_detect(str(cur[0]))
    print len(bboxes)
    i = i + 1
    label = covt_box_matrix(bboxes)
    for k in range(len(label)):
        listbox_filename.insert(i, label[k])
        i += 1
    listbox_filename.insert(i, 'detected object is : %d' % len(bboxes))

    cv2.imshow('detected_output', image)

    k = cv2.waitKey(100)
    if k == 27:
        cv2.destroyAllWindows()
    # if filepath:
    #     entry.insert(0, filepath)  # 将选择好的路径加入到entry里面
    # print (filepath)
    # getdir(filepath)


def getdir(filepath=os.getcwd()):
    """
    用于获取目录下的文件列表
    """
    cf = os.listdir(filepath)
    for i in cf:
        listbox_filename.insert(END, i)


if __name__ == "__main__":
    root = Tk()
    root.title("detected")
    root.geometry("800x600+100+100")
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=8)

    entry = Entry(root, width=80)
    entry.grid(sticky=W + N, row=0, column=0, columnspan=4, padx=5, pady=5)

    button = Button(root, text="选择文件夹", command=callback)

    # root.withdraw()
    # cur = filedialog.askopenfilenames(filetypes=[('text files', '.txt'), ('pythonfiles', ('.py', '.pyw'))])
    #
    # print cur

    button.grid(sticky=W + N, row=1, column=0, padx=5, pady=5)
    # 创建loistbox用来显示所有文件名
    listbox_filename = Listbox(root, width=60)
    listbox_filename.grid(row=2, column=0, columnspan=4, rowspan=4,
                          padx=5, pady=5, sticky=W + E + S + N)

    root.mainloop()
