import pytesseract as pytess
import cv2 as opencv

class OCR():
    def __init__(self):
        pass
    def run(self, image: str) -> str:
        img = opencv.imread(image)

        rgb = opencv.cvtColor(img, opencv.COLOR_BGR2RGB)
        return pytess.image_to_string(rgb)