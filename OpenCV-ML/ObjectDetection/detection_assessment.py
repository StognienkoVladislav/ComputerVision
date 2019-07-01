
import cv2
import numpy as np
import matplotlib.pyplot as plt


def display(conv_img):
    new_img = cv2.cvtColor(conv_img, cv2.COLOR_BGR2RGB)
    plt.imshow(new_img)
    plt.show()


def detect_plate(conv_img):
    plate_img = conv_img.copy()

    plate_rects = plate_cascade.detectMultiScale(plate_img, scaleFactor=1.3, minNeighbors=3)

    for(x, y, w, h) in plate_rects:
        cv2.rectangle(plate_img, (x, y), (x + w, y + h), (0, 0, 255), 4)

    return plate_img


def detect_and_blur_plate(img):

    plate_img = img.copy()
    roi = img.copy()

    plate_rects = plate_cascade.detectMultiScale(plate_img, scaleFactor=1.3, minNeighbors=3)

    for (x, y, w, h) in plate_rects:

        roi = roi[y: y+h, x: x+w]
        blurred_roi = cv2.medianBlur(roi, 7)
        plate_img[y: y+h, x: x+w] = blurred_roi

    return plate_img


img = cv2.imread('../data/car_plate.jpg')
display(img)


plate_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_russian_plate_number.xml')

result = detect_plate(img)
display(result)


blured_plate = detect_and_blur_plate(img)
display(blured_plate)
