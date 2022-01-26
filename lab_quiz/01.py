# 도전과제 1
# 이미지 파일 이름을 입력받아서 해당 파일의 사물 박스 정보 출력하기

import json

f = open('../data/labels/labels.json')
j = json.load(f)

file_name = input()

for l in j:
    if l['name'] == file_name:
        for label in l['labels']:
            if 'box2d' in label:
                print(label['category'], label['box2d'])

# for label in label[0]['labels']:
#     if 'box2d' in label:
#         # print(label.keys())
#         print(label['category'], label['box2d'])