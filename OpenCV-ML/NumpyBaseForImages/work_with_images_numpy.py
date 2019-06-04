import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

pic = Image.open('../data/00-puppy.jpg')

# pic.show()

pic_arr = np.asanyarray(pic)
print(pic_arr.shape)

plt.imshow(pic_arr)
plt.show()


# Red channel values 0 no red, pure black - 255 full pure red
plt.imshow(pic_arr[:, :, 0], cmap='gray')
plt.show()


# Red Mask
pic_red = pic_arr.copy()
pic_red[:, :, 1] = 0
pic_red[:, :, 2] = 0
plt.imshow(pic_red)
plt.show()
