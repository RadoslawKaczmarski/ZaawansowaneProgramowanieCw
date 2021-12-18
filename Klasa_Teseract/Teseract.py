import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'


def sprawdz1zdjecie(img: str):
    return pytesseract.image_to_string(img)


def sprawdzlistezdjec(listazdjec: list):
    return [[pytesseract.image_to_string(zdjecie)] for zdjecie in listazdjec]




