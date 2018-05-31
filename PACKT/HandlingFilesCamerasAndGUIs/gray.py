
import cv2

grayImage = cv2.imread('../data/images.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('MyPicGray.png', grayImage)
