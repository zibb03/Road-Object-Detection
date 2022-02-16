import os

import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('../models/mymodel.h5')

# 임의의 랜덤 이미지 만듬
# rand 는 배열의 차원을 설정할 수 있도록 지원
image = np.random.rand(224, 224, 3)
print(image.shape)

# np.array()를 쓰는 이유 -> 모델에 얼마 만큼의 데이터를 가지고 있는지 알려주기 위하여
data = np.array([image])
print(data.shape)

predict = model.predict(data)
print(predict)

index = np.argmax(predict)
print(index)

# class_names = ['bike', 'bus', 'car', 'motor', 'person', 'rider', 'traffic light', 'traffic sign', 'truck']
class_names = os.listdir('../classification_data')

print(class_names[index])