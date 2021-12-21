import cv2

img = cv2.imread('Zdjecia/a2.jpg')


configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'


classLabels = []
file_name = 'class'
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')


model = cv2.dnn_DetectionModel(frozen_model, configPath)
model.setInputSize(320, 320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)


ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)


for classInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
    cv2.rectangle(img, boxes, color=(0, 255, 0), thickness=2)


cv2.imshow("zdjecie",img)
cv2.waitKey(0)