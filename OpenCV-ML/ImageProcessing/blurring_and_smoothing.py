
import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_img():
    img = cv2.imread('../data/bricks.jpg').astype(np.float32)/255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def display_img(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img)
    plt.show()


sample_img = load_img()
display_img(sample_img)


gamma = 4
result = np.power(sample_img, gamma)
display_img(result)

new_img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(new_img, text='bricks', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=5)
display_img(new_img)

kernel = np.ones(shape=(5, 5), dtype=np.float32) / 25

destination = cv2.filter2D(new_img, -1, kernel)
display_img(destination)


###########################
new_img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(new_img, text='bricks', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=5)

blurred = cv2.blur(new_img, ksize=(5, 5))
display_img(blurred)


###########################
new_img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(new_img, text='bricks', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=5)

gaussian_blurred_img = cv2.GaussianBlur(new_img, (5, 5), 10)
display_img(gaussian_blurred_img)


###########################
new_img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(new_img, text='bricks', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=5)

median_blurred_img = cv2.medianBlur(new_img, 5)
display_img(median_blurred_img)


###########################

sammy_img = cv2.imread('../data/sammy.jpg')

sammy_img = cv2.cvtColor(sammy_img, cv2.COLOR_BGR2RGB)
display_img(sammy_img)

noise_img = cv2.imread('../data/sammy_noise.jpg')
display_img(noise_img)

median = cv2.medianBlur(noise_img, 5)
display_img(median)
