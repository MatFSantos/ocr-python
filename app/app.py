from utils.getPdf import GetPdf
from utils.converter import Converter
from PyPDF2 import PdfReader
import os

filename = GetPdf('https://www.caceres.mt.gov.br/fotos_institucional_downloads/2.pdf').run()

images = Converter(filename=filename).run()

print(len(images))

os.remove(filename)

# print(down('https://drive.google.com/file/d/15tWdhmgSfJ98i6XBuER6_mFH2Vh1Uphg/view?usp=share_link'))
# print(down('https://www.caceres.mt.gov.br/fotos_institucional_downloads/2.pdf'))