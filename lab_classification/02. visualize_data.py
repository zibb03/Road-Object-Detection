import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',
    image_size=(224, 224),
    label_mode='categorical'
)

data = train_dataset.take(1)

plt.figure(0)
plt.title('data')
for images, labels in data:
    for i in range(9):
        # 그래프 속에서 다른 그래프를 그릴 작은 영역을 지정하는 것
        plt.subplot(3, 3, i + 1)
        # 이미지 자료형이 실수로 되어 있으면 에러가 남. 이에 정수형으로 바꿔주는 과정
        plt.imshow(images[i].numpy().astype('uint8'))
        # argmax 는 배열에 들어있는 값중에 가장 큰 값을 구해주는 함수
        # ex) [0, 1, 0, 0, 0, 0, 0, 0, 0] -> 2
        plt.title(train_dataset.class_names[np.argmax(labels[i])])
        plt.axis('off')

plt.show()