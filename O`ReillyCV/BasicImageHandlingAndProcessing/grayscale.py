
from PIL import Image
from matplotlib import pylab
from pylab import *
from numpy.ma import array


# read image to array
im = array(Image.open('data/images.jpeg').convert('L'))

# create a new figure
figure()

# don`t use colors
gray()
imshow(im)
# show contours with origin upper left corner
contour(im, origin='image')
axis('equal')
axis('off')
show()
