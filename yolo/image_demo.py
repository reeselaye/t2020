#! /usr/bin/env python
# coding=utf-8


import cv2
import numpy as np
import core.utils as utils
import tensorflow as tf
from PIL import Image


def image_detect(pic_path):
    return_elements = ["input/input_data:0", "pred_sbbox/concat_2:0", "pred_mbbox/concat_2:0", "pred_lbbox/concat_2:0"]
    pb_file = "./yolov3_coco.pb"
    image_path = pic_path
    # image_path = "/home/liqin/Pictures/60p52.png"
    num_classes = 2
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
    bboxes = utils.postprocess_boxes(pred_bbox, original_image_size, input_size, 0.4)
    print len(bboxes)
    bboxes = utils.nms(bboxes, 0.6, method='nms')
    image, bboxes= utils.draw_bbox(original_image, bboxes)
    # image = Image.fromarray(image)
    image = cv2.resize(image, (image.shape[0] / 5, image.shape[1] / 5))
    # cv2.imshow('aaa', image)
    #
    # k = cv2.waitKey(1000)
    #
    # if k == 27:
    #     cv2.destroyAllWindows()
    return image, bboxes   # break

def conv_box_text(bboxes):

    pass

def main():
    image_path = "/home/liqin/python/relaying/10P1.jpg"
    image, bboxes = image_detect(image_path)
    print bboxes
    conv_box_text(bboxes)



if __name__ == '__main__':
    main()
