
import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_img():
    blank_img = np.zeros((600, 600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img, text='ABCDE', org=(50, 300), fontFace=font, fontScale=5,
                color=(255, 255, 255), thickness=8)
    return blank_img


def display_img(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()


img = load_img()
display_img(img)


kernel1 = np.ones((5, 5), dtype=np.uint8)

result = cv2.erode(img, kernel1, iterations=1)
display_img(result)


white_noise = np.random.randint(low=0, high=2, size=(600, 600))
white_noise = white_noise * 255

noise_image = white_noise + img
display_img(noise_image)

opening = cv2.morphologyEx(noise_image, cv2.MORPH_OPEN, kernel1)
display_img(opening)

black_noise = np.random.randint(low=0, high=2, size=(600, 600))
black_noise = black_noise * (-255)

black_noise_img = img + black_noise
black_noise_img[black_noise_img == -255] = 0
display_img(black_noise_img)

closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel1)
display_img(closing)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel1)
display_img(gradient)
