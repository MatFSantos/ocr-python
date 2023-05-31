import gdown
import uuid


def down(url:str) -> None:

    # Nome do arquivo PDF a ser salvo localmente
    file_name = str(uuid.uuid4()) + '.pdf'

    # Baixar o arquivo PDF
    gdown.download(url, file_name, fuzzy=True)
    return file_name