import cv2
from Pedestrian_detection import show_image


labelsPathText = "coco.names"
weights_path_text = "yolov4-tiny.weights"
config_path_text = "yolov4-tiny.cfg"

image_path = cv2.imread('Zdjecia/a3.jpg')
show_image(labels_path=labelsPathText, weights_path=weights_path_text, config_path=config_path_text, image=image_path)