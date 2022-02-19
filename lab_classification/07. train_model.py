import tensorflow as tf
import os

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',
    image_size=(224, 224),
    # categorical -> 원핫인코딩 방식
    # ex) [0, 1, 0, 0, 0, 0, 0, 0, 0] -> 버스를 나타냄
    # none 일때는 번호로 나타남
    # ex) 2이면 bus 를 나타냄
    label_mode='categorical'
)

model = tf.keras.models.load_model('../models/mymodel.h5')

learning_rate = 0.001

# 학습 방식 정의
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    # optimizer 함수는 loss 값을 줄여들도록 튜닝해주는것
    optimizer=tf.keras.optimizers.RMSprop(learning_rate=learning_rate),
    # 정확도록 보여주도록 하는 옵션
    metrics=['accuracy']
)

# optimizer 함수가 몇번 호출되는지 결정하는 epoch
# 모델 입력 넣어서 학습
model.fit(train_dataset, epochs=5)

if not os.path.exists('../models'):
    os.mkdir('../models')

# ".h5" >> 폴더 형태로 모델을 저장하는 것이 아니라 하나의 파일로 저장해주도록 하는 확장자
model.save('../models/classification_model_trained.h5')