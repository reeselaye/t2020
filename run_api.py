import panel_detect
import image_joint
import r_qrcode
import os

"""

@ ： 文件r_qrcode.py
@API :r_decode(file)
@:param file_name : 图片文件名
@:return : 以字符串形式返回二维码解析结果

"""
def qrcode_r():
    img_file = "img_pano/q1.jpg"
    raw = r_qrcode.r_decode(img_file)
    print("二维码解析内容： ", raw)


"""

@ : 文件 panel_detect.py
API:detected(image_path):
@:param image_path:待识别图片路径
@:returns :
@ sorted_lable :排序后的标签输出 [[0,1,0,1,..],[0,1..],[]]
@ sorted_box:  排序后方框输出 [x_min, y_min, x_max, y_max, possibel,class_id] [421.0, 452,2, 890.0, 870.0, 0.82, 1.0]

"""

def panel_r():
    img_file = "img_qrcode/15.jpg"
    label_out, sorted_box = panel_detect.detected(img_file)
    print(sorted_box)
    print("排序后识别结果", label_out)


"""
@ 文件： joint/image_joint.py
@ API: stich_image_api(path_list,save_path)
@ ：输入的图片文件个数需大于2及以上 
@:param: path_list like ["../img_pano/q1.jpg", "../img_pano/q2.jpg", "../img_pano/q3.jpg"]
@:return 拼接后图片保存位置
"""

def joint_img():
    saved_path = image_joint.stich_image_api(
        ["img_pano/q1.jpg", "img_pano/q2.jpg", "img_pano/q3.jpg"],
        "img_pano/pano1.jpg")

    print("拼接后图像保存于：", os.getcwd(), "/",saved_path)

def main():
    qrcode_r()
    panel_r()
    # joint_img()


if __name__ == '__main__':
    main()
