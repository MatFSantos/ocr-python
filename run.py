import pytesseract
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

print(pytesseract.image_to_string(Image.open("pdf/teste.png")))


# print(pytesseract.image_to_string("pdf/teste.png"))


print(pytesseract.get_languages(config=""))