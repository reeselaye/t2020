#! /usr/bin/env python
# coding=utf-8


import cv2
import numpy as np
import yolo.core.utils as utils
import tensorflow as tf
from PIL import Image
import light

def image_detect(pic_path):
    return_elements = ["input/input_data:0", "pred_sbbox/concat_2:0", "pred_mbbox/concat_2:0", "pred_lbbox/concat_2:0"]
    pb_file = "yolo/yolo.pb"
    image_path = pic_path
    # image_path = "/home/liqin/Pictures/60p52.png"
    num_classes = 3
    input_size = 608
    graph = tf.Graph()

    original_image = cv2.imread(image_path)
    # original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    original_image_size = original_image.shape[:2]
    image_data = utils.image_preporcess(np.copy(original_image), [input_size, input_size])
    image_data = image_data[np.newaxis, ...]

    return_tensors = utils.read_pb_return_tensors(graph, pb_file, return_elements)

    with tf.Session(graph=graph) as sess:
        # saver = tf.train.Saver()
        # saver.restore(sess, './chekpoint/')
        pred_sbbox, pred_mbbox, pred_lbbox = sess.run(
            [return_tensors[1], return_tensors[2], return_tensors[3]],
            feed_dict={return_tensors[0]: image_data})

        # _, summary, train_step_loss, global_step_val = sess.run(
        #                     [train_op, self.write_op, self.loss, self.global_step], feed_dict={
        #                         self.input_data: train_data[0],
        #                         self.label_sbbox: train_data[1],
        #                         self.label_mbbox: train_data[2],
        #                         self.label_lbbox: train_data[3],
        #                         self.true_sbboxes: train_data[4],
        #                         self.true_mbboxes: train_data[5],
        #                         self.true_lbboxes: train_data[6],
        #                         self.trainable: True,
        #                     })

        # print pred_sbbox[0][0][0][0]
        # print pred_sbbox[0][4][0][0][0].shape
        # print pred_mbbox.shape
        # print pred_lbbox.shape

    pred_bbox = np.concatenate((np.reshape(pred_sbbox, (-1, 5 + num_classes)),
                                np.reshape(pred_mbbox, (-1, 5 + num_classes)),
                                np.reshape(pred_lbbox, (-1, 5 + num_classes))), axis=0)

    # pred_bbox = np.concatenate([pred_sbbox,
    #                             pred_mbbox,
    #                             pred_lbbox], axis=0)

    # print pred_bbox
    bboxes = utils.postprocess_boxes(pred_bbox, original_image_size, input_size, 0.3)
    # print("detected ", len(bboxes), "object!!")
    bboxes = utils.nms(bboxes, 0.4, method='nms')
    image, bboxes= utils.draw_bbox(original_image, bboxes)
    # image = Image.fromarray(image)
    # image = cv2.resize(image, (int(image.shape[0] / 5), int(image.shape[1] / 5)))
    # cv2.imshow('aaa', image)
    #
    # k = cv2.waitKey(1000)
    #
    # if k == 27:
    #     cv2.destroyAllWindows()
    return image, bboxes   # break

def conv_box_text(bboxes):
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
    text_matrix = []
    for id, item in enumerate(sort_box):
        if item[5] == 1 or item[5]== 0:
            a.append(int(item[5]))
        # elif item[5] == 3:
        #     a.append('light_off')
        # elif item[5] == 4:
        #     a.append('light_green')
        else:
            a.append(item[5])
        if id < len(sort_box) - 1 and sort_box[id + 1][0] < item[0]:
            text_matrix.append(a)
            a = []
    text_matrix.append(a)
    # print("output : ", text_matrix)

    # 开关状态text_matrix=[[0,1,0,1...],[0,1,...],[]]
    return text_matrix, sort_box
    # pass



"""
API:detected(image_path):
@:param image_path:待识别图片路径
@:returns :
@ sorted_lable :排序后的标签输出 [[0,1,0,1,..],[0,1..],[]]
@ sorted_box:  排序后方框输出 [x_min, y_min, x_max, y_max, possibel,class_id] [421.0, 452,2, 890.0, 870.0, 0.82, 1.0]
"""
def detected(image_path):
    img, bboxes = image_detect(image_path)
    for i, bbox in enumerate(bboxes):
        if bbox[5] ==2 or bbox[5]== '2':
            light_status = light.detected_light(img, bbox)
            bboxes[i][5] = light_status
    sorted_label, sorted_box = conv_box_text(bboxes)
    return sorted_label, sorted_box


def main():
    image_path = "/home/liqin/python/relaying/10P1.jpg"
    img = cv2.imread(image_path)
    # light.detected_light(img,[3942,455,4329,842])
    label_out, sorted_box = detected(image_path)
    image, bboxes = image_detect(image_path)
    print(bboxes)
    label_out, sorted_box = conv_box_text(bboxes)
    print(label_out)
    print(len(sorted_box),"++",sorted_box)
    # cv2.imshow("output",image)
    # cv2.waitKey(5000)



if __name__ == '__main__':
    main()


