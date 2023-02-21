from PIL import Image
from detector import detect_faces
import os
from tqdm import tqdm

path = 'E:/face_test/RFW_test_jpg/data/African'
path_Align = 'E:/face_test/RFW_test_jpg/data/African_Align'
count = 0
for sub_folder in tqdm(os.listdir(path)):
    # if not os.path.isdir(path_Align):
    #     os.mkdir(path_Align)
    for image_name in os.listdir(os.path.join(path, sub_folder)):
        img = Image.open(os.path.join(path, sub_folder, image_name))
        try:
            _, landmarks = detect_faces(img)
        except Exception:
            print("{} is discarded due to exception!".format(os.path.join(path, sub_folder, image_name)))
            continue
        if len(landmarks) == 0:
            print("{} is discarded due to non-detected landmarks!".format(
                os.path.join(path, sub_folder, image_name)))
            continue


        # 将图片路径写入txt文件，图片数量以及内容和landmark文件一致
        with open('img_list.txt', 'a') as f:
            f.write(os.path.join(path, sub_folder, image_name).replace('\\', '/'))
            f.write('\n')


        # 将图片路径和landmark文件写入txt文件
        with open('RFW_African_lmk.txt', 'a') as f:
            data = [landmarks[0][0], landmarks[0][5], landmarks[0][1], landmarks[0][6], landmarks[0][2], landmarks[0][7], landmarks[0][3], landmarks[0][8], landmarks[0][4], landmarks[0][9]]
            f.write(os.path.join(path, sub_folder, image_name).replace('\\', '/'))
            f.write(" ")
            for d in data:
                d = round(d, 4)
                f.write(str(d))
                f.write(" ")
            f.write("\n")

        #将图片路径和标签写入txt文件

        with open('index_file_old.txt', 'a') as f:
            f.write(os.path.join(path, sub_folder, image_name).replace('\\', '/'))
            f.write('\t')
            f.write(str(count))
            f.write('\n')
    count = count+1
