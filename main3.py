import cv2

img = cv2.imread('Zdjecia/a2.jpg')


configPath = 'a1.pbtxt'
weightsPath = 'efficientdet-d0.pb'


cv2.imshow('Zdjecie', img)
cv2.waitKey(0)


classNames = []
classFile = 'Klasy'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')


net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(100, 100)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


classIDS, confs, bbox = net.detect(img, confThreshold=0.5)


for classID, confidence, box in zip(classIDS.flatten(), confs.flatten(), bbox):
    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)

