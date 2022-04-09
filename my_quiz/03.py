# 도전과제 3
# 이미지 파일 이름을 입력받아서 해당 이미지의 각 사물 박스를
# 개별 이미지로 잘라내어 사물별로 폴더에 나누어 저장해보기
#
# 나의 코드
# import cv2
# import json
# import os
#
# f = open("../data/labels/labels.json")
# label = json.load(f)
#
# if not os.path.exists('../classification_data'):
#     os.mkdir('../classification_data')
#
# cnt = 0
#
# for i in range(12):
#     file_name = label[i]['name']
#     image = cv2.imread("../data/images/" + file_name)
#
#     for l in label[i]['labels']:
#         if 'box2d' in l:
#             x1 = (l['box2d']['x1'])
#             y1 = (l['box2d']['y1'])
#             x2 = (l['box2d']['x2'])
#             y2 = (l['box2d']['y2'])
#
#             crop_image = image[int(y1):int(y2), int(x1):int(x2)]
#             crop_name = l['category']
#
#             if not os.path.exists('../classification_data/' + crop_name):
#                 os.mkdir('../classification_data/' + crop_name)
#
#             save_name = '/' + str(cnt) + '.jpg'
#             cv2.imwrite('../classification_data/' + crop_name + save_name, crop_image)
#             cnt += 1
#
# print(cnt)

import cv2
import json
import os

file_names = os.listdir('../data/images')

f = open('../data/labels/labels.json')
labels = json.load(f)

if not os.path.exists('../classification_data'):
    os.mkdir('../classification_data')

cnt = 0

for label in labels:
    if label['name'] in file_names:
        image = cv2.imread('../data/images/' + label['name'])
        for box in label['labels']:
            if 'box2d' in box:
                x1 = int(box['box2d']['x1'])
                y1 = int(box['box2d']['y1'])
                x2 = int(box['box2d']['x2'])
                y2 = int(box['box2d']['y2'])
                crop_image = image[y1:y2+1, x1:x2+1]
                # 범위가 미만이어서 +1 해준 것

                if not os.path.exists('../classification_data/' + box['category']):
                    os.mkdir('../classification_data/' + box['category'])

                # cv2.imwrite('../classification_data/' + box['category'] + '/' + str(cnt) + '.jpg', crop_image)
                cv2.imwrite(f'../classification_data/{box["category"]}/{str(cnt)}.jpg', crop_image)
                cnt += 1