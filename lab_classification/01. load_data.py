import tensorflow as tf

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',
    image_size=(224, 224),
    # categorical -> 원핫인코딩 방식
    # ex) [0, 1, 0, 0, 0, 0, 0, 0, 0] -> 버스를 나타냄
    # none 일때는 번호로 나타남
    # ex) 2이면 bus 를 나타냄
    label_mode='categorical'

)

data = train_dataset.take(1)
for images, labels in data:
    print(images, labels)

print(train_dataset.class_names)