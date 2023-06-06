from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from app.utils.getPdf import GetPdf
from app.utils.converter import Converter
from app.utils.ocr import OCR

app = Flask(__name__)
CORS(app)

@app.route("/ocr", methods=['POST'])
def ocr():
    link = request.json.get("link") # link da requisição
    filename = GetPdf(url=link).run()   # faz o download do pdf 
    images = Converter(filename=filename).run() #converte as páginas do pdf em imagem
    os.remove(filename) #deleta o pdf do disco
    my_ocr = OCR()
    strs = []
    for image in images:
        strs.append(my_ocr.run(image)) #faz a leitura das imagens utilizando o OCR
        os.remove(image)    # deleta as imagens que foram salvas
    return jsonify({"strings": strs}), 200


@app.route("/", methods=['GET'])
def hello():
    data = {"message" : "hello world" }
    return jsonify(data)

# https://drive.google.com/file/d/15tWdhmgSfJ98i6XBuER6_mFH2Vh1Uphg/view?usp=share_link
# https://www.caceres.mt.gov.br/fotos_institucional_downloads/2.pdf