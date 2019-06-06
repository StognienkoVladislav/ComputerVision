
import cv2
import numpy as np
import matplotlib.pyplot as plt


dark_horse = cv2.imread('../data/horse.jpg')
show_horse = cv2.cvtColor(dark_horse, cv2.COLOR_BGR2RGB)

rainbow = cv2.imread('../data/rainbow.jpg')
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

blue_bricks = cv2.imread('../data/bricks.jpg')
show_blue_bricks = cv2.cvtColor(blue_bricks, cv2.COLOR_BGR2RGB)

hist_values = cv2.calcHist([dark_horse], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist_values)
plt.show()


#################################################################
color = ('b', 'g', 'r')
img = blue_bricks

for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.title('Hist for Blue Bricks')
plt.show()


#################################################################
img = cv2.imread('../data/rainbow.jpg')
show_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

mask = np.zeros(img.shape[:2], np.uint8)

mask[300:400, 100:400] = 255

masked_img = cv2.bitwise_and(img, img, mask=mask)
show_mask_img = cv2.bitwise_and(show_img, show_img, mask)

plt.imshow(masked_img)
plt.show()

hist_mask_values_red = cv2.calcHist([rainbow], channels=[2], mask=mask, histSize=[256], ranges=[0, 256])

plt.plot(hist_mask_values_red)
plt.show()


def display_img(sample):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(sample, cmap='gray')
    plt.show()


gorilla = cv2.imread('../data/gorilla.jpg', 0)
display_img(gorilla)

hist_values = cv2.calcHist([gorilla], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist_values)
plt.show()

eq_gorilla = cv2.equalizeHist(gorilla)
display_img(eq_gorilla)


hsv = cv2.cvtColor(gorilla, cv2.COLOR_BGR2HSV)
hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])
eq_color_gorilla = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
display_img(eq_color_gorilla)
