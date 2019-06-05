
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('../data/00-puppy.jpg')
plt.imshow(img)
plt.show()

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.show()
