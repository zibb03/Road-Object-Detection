import cv2

file_name = '34811fce-1c9200fe.jpg'
image = cv2.imread("../data/images/" + file_name)

cv2.putText(image, 'PYTHON', (100, 100), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', image)
cv2.waitKey(0)
