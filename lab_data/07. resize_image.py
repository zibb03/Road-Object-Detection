import cv2

file_name = '34811fce-1c9200fe.jpg'
image = cv2.imread("../data/images/" + file_name)

# (x, y)
resize_image = cv2.resize(image, (224, 224))

cv2.imshow('image', image)
cv2.imshow('resize image', resize_image)
cv2.waitKey(0)