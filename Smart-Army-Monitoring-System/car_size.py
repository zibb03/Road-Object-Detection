import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
from matplotlib import pyplot as plt

child = 'D:/GitHub/Road-Object-Detection/ionic_front.jpg'
image = cv2.imread(child, cv2.IMREAD_UNCHANGED)

'''
grayImage = cv2.imread(child, cv2.IMREAD_GRAYSCALE)

face_cascade = cv2.CascadeClassifier(
    'C:/Users/user/PycharmProjects/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
face = face_cascade.detectMultiScale(grayImage, 1.01, 10)
eye_cascade = cv2.CascadeClassifier(
    'C:/Users/user/PycharmProjects/OpenCV/haarcascades/haarcascade_eye.xml')
eye = eye_cascade.detectMultiScale(grayImage, 1.01, 10)

for (x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

    face_image_gray = grayImage[y:y + h, x:x + w]
    face_image_color = image[y:y + h, x:x + w]

    faces_in_body = face_cascade.detectMultiScale(face_image_gray)

    eyes_in_faces = eye_cascade.detectMultiScale(face_image_gray)
    for (xf, yf, wf, hf) in eyes_in_faces:
        print(xf, yf, wf, hf)
        cv2.rectangle(face_image_color, (xf, yf), (xf + wf, yf + hf), (0, 255, 0), 2)
'''

x = 250
y = 540
w = 250
h = 130
x2 = 170
y2 = 130
w2 = 950
h2 = 700

# 1204 X 904
img = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
# cv2.putText(image, '60저', (x, y - 5),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 3)

# For bounding box
# img = cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

label = '60저 7697'

# For the text background
# Finds space required by the text so that we can put a background with that amount of width.
(w, h), _ = cv2.getTextSize(
    label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)

# Prints the text.
img = cv2.rectangle(img, (x, y - 20), (x + w, y), (255, 0, 0), -1)

label = '준중형'

(w2, h2), _ = cv2.getTextSize(
    label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)

img = cv2.rectangle(img, (x2, y2 - 20), (x2 + w2, y2), (0, 255, 0), -1)

# img = cv2.putText(img, label, (x, y - 5),
#                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

# For printing text
# img = cv2.putText(img, 'test', (x, y),
#                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

fontpath = "fonts/gulim.ttc"
font = ImageFont.truetype(fontpath, 20)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
# draw.text((x, y - 20),  "60저 7697", font=font, fill=(255, 255, 255, 0))
draw.text((x2, y2 - 20),  "준중형", font=font, fill=(255, 255, 255, 0))

font = ImageFont.truetype(fontpath, 50)
draw.text((900, 20),  "등록된 차량", font=font, fill=(0, 255, 0, 0))
img = np.array(img_pil)



cv2.imshow("res", img)
cv2.waitKey()
cv2.destroyAllWindows()

#
# plt.figure(figsize=(12, 12))
# plt.imshow(img)
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()