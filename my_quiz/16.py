import yolov3

import cv2
import os

model = yolov3.YOLO_V3()
model.build()
model.load()

path = '../data/videos/cabc30fc-e7726578.mov'
cap = cv2.VideoCapture(path)

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

if not os.path.exists('../outputs'):
    os.mkdir('../outputs')

# print(fourcc, fps, width, height)
out = cv2.VideoWriter('../outputs/output.wmv', fourcc, fps, (width, height))

now_frame = 1

while cap.isOpened():
    ret, image = cap.read()

    if not ret:
        break

    result = model.predict(image)
    # cv2.imshow('image', img)
    # cv2.imshow('result', result)

    out.write(result)
    # if cv2.waitKey(1) == ord('q'):
    #     break

    # print(f"{now_frame} / {frame_count} : {now_frame / frame_count}%")
    print(f"{now_frame} / {frame_count}")
    now_frame += 1

cap.release()
out.release()