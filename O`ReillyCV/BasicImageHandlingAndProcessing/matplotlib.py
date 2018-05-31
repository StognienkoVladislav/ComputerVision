
from PIL import Image
from matplotlib import pylab
from numpy.ma import array
from pylab import *


# read image to array

im = array(Image.open('data/images.jpeg'))

# plot the image
imshow(im)

# some points
x = [10, 10, 40, 40]
y = [20, 50, 20, 50]

# plot the points with red star-markers
plot(x, y, 'r*')

# line plot connecting the first two points
plot(x[:2], y[:2])

# add title and show the plot
title('Plotting: "images.jpeg"')
axis('off')

plot(x, y)              # default blue solid line
plot(x, y, 'r*')        # red star-markers
plot(x, y, 'go-')       # green line with circle-markers
plot(x, y, 'ks:')       # black dotted line with square-markers
show()
