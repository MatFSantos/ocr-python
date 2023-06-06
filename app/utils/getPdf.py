from gdown import download
from uuid import uuid4

class GetPdf():
    def __init__(self, url: str):
        self.__url = url

    def run(self):
        file_name = 'pdf/' +  str(uuid4()) + '.pdf'
        
        download(self.__url, file_name, fuzzy=True, quiet=True)

        return file_name
