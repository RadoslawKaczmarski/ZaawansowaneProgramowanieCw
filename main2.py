from __future__ import print_function
from imutils.object_detection import non_max_suppression
import numpy as np
import imutils
import cv2

imagePath = 'Zdjecia/a7.jpg'

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

image = cv2.imread(imagePath)
image = imutils.resize(image, width=min(550, image.shape[1]))
orig = image.copy()

(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

for (x, y, w, h) in rects:
    cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

for (xA, yA, xB, yB) in pick:
    cv2.rectangle(image, (xA, yA), (xB, yB), (255, 0, 0), 2)

filename = imagePath[imagePath.rfind("/") + 1:]
print("[INFO] {}: {} boxes".format(filename, len(pick)))


cv2.imshow("Image pedestrians", image)
cv2.waitKey(0)
