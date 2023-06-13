from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import re
from app.utils.getPdf import GetPdf
from app.utils.converter import Converter
from app.utils.ocr import OCR
from app.utils.match import match

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
        strs.append(my_ocr.run(image).replace("\n\n", "").replace("\n", " ")) #faz a leitura das imagens utilizando o OCR
        os.remove(image)    # deleta as imagens que foram salvas

    num_ano = match(r"N° (\d+/\d+)", strs[0])
    if num_ano:
        num = num_ano.split("/")[0]
        ano = num_ano.split("/")[1]
        ano = "19" + ano if int(ano) > 23 and int(ano) < 99 else ano
    else:
        num = None
        ano = None
    
    cabecalho = match(r"N° \d+/\d+\n\n(.*?)\n\nRESOLVE:", strs[0], dotAll=True)
    
    reitor = match(r"(.*)\sREITOR", strs[0])

    if not reitor:
        reitor = match(r"(.*)\n\nReitor", strs[0])


    data = match(r"(.*)\s" + ano if ano else None, strs[len(strs) - 1])

    data = data.split(',')[1] + " " + ano if data else None

    return jsonify({
        "numero": num + "/" + ano if num and ano else None,
        "ano": ano,
        "data": data,
        "reitor": reitor,
        "cabecalho": cabecalho.replace("\n", " ") + " RESOLVE:" if cabecalho else None,
        "texto": " ".join(strs),
        "link":link
    }), 200


@app.route("/", methods=['GET'])
def hello():
    data = {"message" : "hello world" }
    return jsonify(data)

# https://drive.google.com/file/d/15tWdhmgSfJ98i6XBuER6_mFH2Vh1Uphg/view?usp=share_link
# https://www.caceres.mt.gov.br/fotos_institucional_downloads/2.pdf