import tensorflow as tf

model = tf.keras.applications.MobileNet(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

# imagenet 가중치를 가져왔는데, 이를 학습시키지 않기 위한 코드
model.trainable = False

model = tf.keras.Sequential([
    model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(9),
    tf.keras.layers.Softmax()
])

model.summary()