import cv2

file_name = '34811fce-1c9200fe.jpg'
image = cv2.imread("../data/images/" + file_name)

#BGR
cv2.rectangle(image, (10, 10), (100, 100), (0, 0, 255), 3)

cv2.imshow('image', image)
cv2.waitKey(0)