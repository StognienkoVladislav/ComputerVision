
import cv2
import numpy as np
import matplotlib.pyplot as plt

nadia = cv2.imread('../data/Nadia_Murad.jpg', 0)
denis = cv2.imread('../data/Denis_Mukwege.jpg', 0)
solvay = cv2.imread('../data/solvay_conference.jpg', 0)
# plt.imshow(solvay, cmap='gray')
# plt.show()


face_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')


def detect_face(img):

    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img)

    for (x, y, w, h) in face_rects:

        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
    return face_img


result = detect_face(solvay)
plt.imshow(result, cmap='gray')
plt.show()


eye_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_eye.xml')


def detect_eyes(img):

    face_img = img.copy()

    eye_rectangels = eye_cascade.detectMultiScale(face_img, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in eye_rectangels:

        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
    return face_img


result = detect_eyes(nadia)
plt.imshow(result, cmap='gray')
plt.show()


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    cv2.imshow('Video Face Detect', frame)
    k = cv2.waitKey(1)

    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
