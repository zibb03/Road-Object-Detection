import os
import tensorflow as tf
import numpy as np
import cv2

category = str(input())
number = str(input())

model = tf.keras.models.load_model('../models/mymodel.h5')

image = cv2.imread("../classification_data/" + category + "/" + number + ".jpg")
print(image.shape)

resize_image = cv2.resize(image, (224, 224))

data = np.array([resize_image])
print(data.shape)

predict = model.predict(data)
print(predict)

index = np.argmax(predict)
print(index)

class_names = os.listdir('../classification_data')

print(class_names[index])

cv2.imshow('image', image)
cv2.waitKey(0)
