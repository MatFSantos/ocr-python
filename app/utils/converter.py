from pdf2image import convert_from_path
from uuid import uuid4

class Converter():
    def __init__(self, filename: str):
        self.__filename = filename
    
    def run(self) -> list[str] :
        images = convert_from_path(self.__filename)
        
        urls = []
        
        for i, image in enumerate(images):
            image_path = f"img/img_{str(uuid4())}.jpg"
            image.save(image_path, "JPEG")
            urls.append(image_path)

        return urls

