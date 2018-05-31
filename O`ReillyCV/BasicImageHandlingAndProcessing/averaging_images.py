from PIL import Image
from matplotlib import pylab
from pylab import *
from numpy.ma import array


def compute_average(imlist):
    """Compute the average of a list of images."""

    # open first image and make into a rray of type float
    averageim = array(Image.open(imlist[0]), 'f')

    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except Exception as e:
            print(imname + '...skipped')
    averageim /= len(imlist)

    return array(averageim, 'uint8')
