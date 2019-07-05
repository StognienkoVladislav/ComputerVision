
import matplotlib.pyplot as plt

from keras.datasets import mnist
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten

from sklearn.metrics import classification_report


(x_train, y_train), (x_test, y_test) = mnist.load_data()

y_cat_test = to_categorical(y_test, 10)
y_cat_train = to_categorical(y_train, 10)

x_train = x_train / x_train.max()  # /255
x_test = x_test / x_test.max()

x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

model = Sequential()

# Convolution layer
model.add(Conv2D(filters=32, kernel_size=(4, 4), input_shape=(28, 28, 1), activation='relu'))

# Pooling layer
model.add(MaxPool2D(pool_size=(2, 2)))

# 2d --> 1d
model.add(Flatten())

# Dense layer
model.add(Dense(128, activation='relu'))

model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

model.summary()
model.fit(x_train, y_cat_train, epochs=2)

print(model.metrics_names)

model.evaluate(x_test, y_cat_test)


predictions = model.predict_classes(x_test)
print(classification_report(y_test, predictions))
