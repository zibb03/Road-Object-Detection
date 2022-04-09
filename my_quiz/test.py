import model

import tensorflow as tf

Model = model.Model()
Model.load()
Model.load_data()

predict = Model.predict('../classification_data/car/16.jpg')
print(predict)