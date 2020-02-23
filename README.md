# t2020
==

#requiement
    python3.6
    pip3 install -r requirements.txt

#API详见.py文件  
    二维码识别
    @ ： 文件r_qrcode.py
    @API :r_decode(file)
    @:param file_name : 图片文件名
    @:return : 以字符串形式返回二维码解析结果

    压板/指示灯
    @ : 文件 panel_detect.py
    API:detected(image_path):
    @:param image_path:待识别图片路径
    @:returns :
    @ sorted_lable :排序后的标签输出 [[0,1,0,1,..],[0,1..],[]]
    @ sorted_box:  排序后方框输出 [x_min, y_min, x_max, y_max, possibel,class_id] [421.0, 452,2, 890.0, 870.0, 0.82, 1.0]    
    
    拼接
    @ 文件： joint/image_joint.py
    @ API: stich_image_api(path_list,save_path)
    @ ：输入的图片文件个数需大于2及以上 
    @:param: path_list like ["../img_pano/q1.jpg", "../img_pano/q2.jpg", "../img_pano/q3.jpg"]
    @:return 拼接后图片保存位置
    
    
#test
    python3 run_api.py

#文件夹
    *.xml 标签文件
    *.pb  网络参数文件
    joint/ 拼接
    yolo/  识别检测网络框架
    

