import cv2
from Pedestrian_detection import show_image
import os

directory = 'Zdjecia'

L1 = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    L1.append(f)

labelsPathText = "Models/coco.names"
weights_path_text = "Models/yolov4-tiny.weights"
config_path_text = "Models/yolov4-tiny.cfg"

for image in L1:
    show_image(labels_path=labelsPathText, weights_path=weights_path_text,
               config_path=config_path_text, image=cv2.imread(image))
