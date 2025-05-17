import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
from matplotlib import pyplot as plt

child = 'D:/GitHub/Road-Object-Detection/thermal_face.jpg'
image = cv2.imread(child, cv2.IMREAD_UNCHANGED)

x = 100
y = 100
w = 270
h = 300
x2 = 170
y2 = 130
w2 = 950
h2 = 700

# 1024 X 461
img = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
# cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 3)

label = '등록된 사용자'

# For the text background
# Finds space required by the text so that we can put a background with that amount of width.
(w, h), _ = cv2.getTextSize(
    label, cv2.FONT_HERSHEY_SIMPLEX, 1, 40)

# Prints the text.
img = cv2.rectangle(img, (10, 10), (260, 50), (255, 0, 0), -1)

# For bounding box
# img = cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


# img = cv2.putText(img, label, (x, y - 5),
#                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

# For printing text
# img = cv2.putText(img, 'test', (x, y),
#                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

fontpath = "fonts/gulim.ttc"
font = ImageFont.truetype(fontpath, 20)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)

font = ImageFont.truetype(fontpath, 40)
draw.text((10, 10),  "등록된 사용자", font=font, fill=(255, 255, 255, 0))
img = np.array(img_pil)


cv2.imshow("res", img)
cv2.waitKey()
cv2.destroyAllWindows()

