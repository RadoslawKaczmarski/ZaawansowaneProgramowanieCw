import numpy as np
import cv2
import imutils


NMS_THRESHOLD = 0.6
MIN_CONFIDENCE = 0.2


def pedestrian_detection(image, model, layer_name, personidz=0):
	(H, W) = image.shape[:2]
	results = []

	blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
	model.setInput(blob)
	layer_outputs = model.forward(layer_name)

	boxes = []
	centroids = []
	confidences = []

	for output in layer_outputs:
		for detection in output:

			scores = detection[5:]
			class_id = np.argmax(scores)
			confidence = scores[class_id]

			if class_id == personidz and confidence > MIN_CONFIDENCE:

				box = detection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")

				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))

				boxes.append([x, y, int(width), int(height)])
				centroids.append((centerX, centerY))
				confidences.append(float(confidence))

	idzs = cv2.dnn.NMSBoxes(boxes, confidences, MIN_CONFIDENCE, NMS_THRESHOLD)

	if len(idzs) > 0:
		for i in idzs.flatten():
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])
			res = (confidences[i], (x, y, x + w, y + h), centroids[i])
			results.append(res)
	return results


def show_image(labels_path, weights_path, config_path, image):
	labels = open(labels_path).read().strip().split("\n")

	model = cv2.dnn.readNetFromDarknet(config_path, weights_path)

	layer_name = model.getLayerNames()
	layer_name = [layer_name[i - 1] for i in model.getUnconnectedOutLayers()]

	image = imutils.resize(image, width=700)
	results = pedestrian_detection(image, model, layer_name, personidz=labels.index("person"))

	for res in results:
		cv2.rectangle(image, (res[1][0], res[1][1]), (res[1][2], res[1][3]), (0, 255, 0), 2)

	cv2.imshow("Detection Image", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


