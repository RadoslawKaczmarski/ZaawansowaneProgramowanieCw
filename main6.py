import cv2
import imutils
from main5 import Detect


img = cv2.imread("Zdjecia/a12.jpeg")
img = imutils.resize(img,width=900)

img = Detect(img)
cv2.waitKey(0)
cv2.destroyAllWindows()