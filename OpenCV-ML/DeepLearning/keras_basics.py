
import cv2
import numpy as np

from numpy import genfromtxt

from keras.layers import Dense
from keras.models import Sequential, load_model

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


data = genfromtxt('../data/bank_note_data.txt', delimiter=',')

labels = data[:, 4]
features = data[:, 0:4]

X = features
y = labels


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
scaler_object = MinMaxScaler()

scaler_object.fit(X_train)
scaled_X_train = scaler_object.transform(X_train)
scaled_X_test = scaler_object.transform(X_test)

model = Sequential()
model.add(Dense(4, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(scaled_X_train, y_train, epochs=50, verbose=2)

predictions = model.predict_classes(scaled_X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

model.save("sample_model.h5")

new_model = load_model('sample_model.h5')
