import cv2

file_name = '00e9be89-00001215.jpg'
image = cv2.imread("../data/images/" + file_name)

cv2.imshow('image', image)
cv2.waitKey(0)