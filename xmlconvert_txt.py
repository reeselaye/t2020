import sys
import os
import glob
import xml.etree.ElementTree as ET

# # change directory to the one with the files to be changed
# path_to_folder = '../ground-truth'
# #print(path_to_folder)
# os.chdir(path_to_folder)
#
# # old files (xml format) will be moved to a "backup" folder
# ## create the backup dir if it doesn't exist already
# if not os.path.exists("backup"):
#   os.makedirs("backup")
#
# # create VOC format files
# xml_list = glob.glob('*.xml')
# if len(xml_list) == 0:
#   print("Error: no .xml files found in ground-truth")
#   sys.exit()

xml_list = os.listdir('num/')
for tmp_file in xml_list:
    # print(tmp_file)
    # 1. create new file (VOC format)
    # with open('../ground-truth/' + tmp_file, "r") as of:
    new_f = open('train.txt', 'a')

    root = ET.parse('num/' + tmp_file).getroot()
    img_path = root.find('path').text
    new_f.write(img_path + " ")
    size = root.find('size')
    width = size.find('width').text
    height = size.find('height').text
    for obj in root.findall('object'):
        obj_name = obj.find('name').text
        bndbox = obj.find('bndbox')
        left = bndbox.find('xmin').text
        top = bndbox.find('ymin').text
        right = bndbox.find('xmax').text
        bottom = bndbox.find('ymax').text
        if int(right)>int(width) or int(bottom)>int(height):
            print ("eaaa!!")
            continue
        if int(right)<0 or int(bottom)<0:
            print ("err!!")
            continue
            # print("over!!!")
            # print (img_path)
            # print (obj_name)

        if obj_name == 'light_red':
            obj_name = '2'
        elif obj_name == 'light_off':
            obj_name = '2'
        elif obj_name == 'light_green':
            obj_name = '2'
        elif obj_name =='0':
            pass
        elif obj_name =='1':
            pass
        elif obj_name == '2':
            pass
        else:
            continue
        new_f.write(left + "," + top + "," + right + "," + bottom + "," + obj_name + " ")
    new_f.write("\n")
    # 2. move old file (xml format) to backup
    # os.rename(tmp_file, "backup/" + tmp_file)
    new_f.close()
print("Conversion completed!")
