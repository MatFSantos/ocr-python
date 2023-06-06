from typing import Any
from pytesseract import  image_to_string

class OCR():
    def __init__(self):
        pass
    def run(self, image: Any) -> str:
        return image_to_string(image, lang="pt")