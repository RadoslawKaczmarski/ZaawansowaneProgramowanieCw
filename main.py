
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'

print(pytesseract.image_to_string(Image.open('Zdjecia/nowoczesna.jpg')))

