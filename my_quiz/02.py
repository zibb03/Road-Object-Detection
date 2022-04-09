# 도전과제 2
# 이미지 파일 이름을 입력받아서 해당 이미지에 사물 박스와 사물 이름을 그려서 화면에 띄우기

import cv2
import json

# file_name = '34811fce-1c9200fe.jpg'
# image = cv2.imread("../data/images/" + file_name)

f = open("../data/labels/labels.json")
label = json.load(f)

# for i in range(12):
#     file_name = label[i]['name']
#     print(file_name)

for i in range(12):
    file_name = label[i]['name']
    image = cv2.imread("../data/images/" + file_name)

    for l in label[i]['labels']:
        if 'box2d' in l:
            x1 = (l['box2d']['x1'])
            y1 = (l['box2d']['y1'])
            x2 = (l['box2d']['x2'])
            y2 = (l['box2d']['y2'])

            # print(label['category'], label['box2d'])
            cv2.rectangle(image, pt1=(int(x1), int(y1)), pt2=(int(x2), int(y2)), thickness=2, color=(0, 0, 255), lineType=cv2.LINE_AA)
            # print(l['category'])
            cv2.putText(image, l['category'], org=(int(x1), int(y1)), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.8, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)

    cv2.imshow('image', image)
    cv2.waitKey(0)

