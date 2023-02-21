import os
from tqdm import tqdm

count_lmk = 0
with open('RFW_African_lmk.txt', 'r') as f:
    for line in f:
        count_lmk = count_lmk + 1
        line = line.rstrip().split(' ')  # 每行以空格分隔的内容，内容放在列表中
        print(line[1:])


print('landmarks文件图片数量:', count_lmk)

count_img = 0
with open('img_list.txt', 'r') as f:
    for line in f:
        count_img = count_img+1
print('图片列表文件数量：', count_img)

path = 'E:/face_test/RFW_test_jpg/data/African'
path_Align = 'E:/face_test/RFW_test_jpg/data/African_Align'
filename = 'RFW_African_lmk.txt'
count_img_ori = 0
for sub_folder in tqdm(os.listdir(path)):
    # if not os.path.isdir(path_Align):
    #     os.mkdir(path_Align)
    for image_name in os.listdir(os.path.join(path, sub_folder)):
        count_img_ori = count_img_ori+1
print('原始文件夹图片数量：', count_img_ori)
