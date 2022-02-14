import tensorflow as tf
import os

model = tf.keras.applications.MobileNet(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

model.trainable = False

model = tf.keras.Sequential([
    model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(9),
    tf.keras.layers.Softmax()
])

model.summary()

if not os.path.exists('../models'):
    os.mkdir('../models')

# ".h5" >> 폴더 형태로 모델을 저장하는 것이 아니라 하나의 파일로 저장해주도록 하는 확장자
model.save('../models/mymodel.h5')