import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'

img = cv2.imread('Zdjecia/img2.jpg')
img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_convert = converted_img = cv2.threshold(cv2.GaussianBlur(img_convert, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img_convert = cv2.threshold(cv2.bilateralFilter(img_convert, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img_convert = cv2.threshold(cv2.medianBlur(img_convert, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img_convert = cv2.adaptiveThreshold(cv2.GaussianBlur(img_convert, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

img_convert = cv2.adaptiveThreshold(cv2.bilateralFilter(img_convert, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

img_convert = cv2.adaptiveThreshold(cv2.medianBlur(img_convert, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

cv2.imshow('image', img_convert)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(pytesseract.image_to_string(img_convert))
