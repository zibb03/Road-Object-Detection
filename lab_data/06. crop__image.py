import cv2

# file_name = '00e9be89-00001215.jpg'
file_name = '34811fce-1c9200fe.jpg'
image = cv2.imread("../data/images/" + file_name)

# image[10이상:100미만, 10이상:100미만]
crop_image = image[10:100, 10:100]

cv2.imshow('image', image)
cv2.imshow('crop_image', crop_image)
cv2.waitKey(0)