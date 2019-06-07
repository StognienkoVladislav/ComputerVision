
import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_img(img, cmap=None):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap)
    plt.show()


img = cv2.imread('../data/giraffes.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
display_img(img)


ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
display_img(thresh1)

kernel = np.ones(shape=(4, 4), dtype=np.float32) / 10

result = cv2.filter2D(img, -1, kernel=kernel)
display_img(result)


sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
display_img(sobelx)

colors = ['b', 'g', 'r']

for i, col in enumerate(colors):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)

plt.title("My hist")
plt.show()
