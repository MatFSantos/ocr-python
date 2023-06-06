from typing import Any
from PyPDF2 import PdfReader

class Converter():
    def __init__(self, filename: str):
        self.__filename = filename
    
    def run(self) -> list[Any] :
        file = open(self.__filename, 'rb')
        pdf_reader = PdfReader(file)
        
        images = []
        
        for page in range(len(pdf_reader.pages)):
            pdf_page = pdf_reader.pages[page]
            images.append(pdf_page.extract_text())
        file.close()
        return images

