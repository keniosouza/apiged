import os
import cv2
import pytesseract
import numpy as np
import base64


class ImageToText:

    # Inicialização da classe
    def __init__(self, base64_string: str):

        # Armazena a string Base64 em uma variável
        self._base64_string = base64_string

        # Caminho absoluto do Tesseract
        self._tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        # Controles
        self._image = None
        self._text = ""
        self._base64 = ""
        self._message_error = ""

        # Verifica se o Base64 foi informado
        if self._base64_string:

            try:
                # Decodifica a string Base64 para bytes
                self._base64_bytes = base64.b64decode(self._base64_string)

                # Converte os bytes em um numpy array (requerido pelo OpenCV)
                np_arr = np.frombuffer(self._base64_bytes, np.uint8)

                # Decodifica a imagem em formato OpenCV (BGR)
                self._image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

                # Verifica se a imagem foi carregada corretamente
                if self._image is None:
                    self._message_error = "Erro ao carregar a imagem a partir da Base64"
                    return None

                # Processa a imagem
                pytesseract.pytesseract.tesseract_cmd = self._tesseract

                # Converte o texto da imagem para uma string, informando a linguagem português como padrão
                self._text = pytesseract.image_to_string(
                    self._image, lang="por")

                # Armazena o conteúdo em Base64
                self._base64 = base64.b64encode(self._text.encode('utf-8'))

            except Exception as e:
                self._message_error = f"Erro ao processar a imagem: {e}"
                return None

        else:
            self._message_error = "Nenhum arquivo Base64 informado"
            return None

    # Retorna o Base64 do arquivo Word gerado
    def get_base64(self) -> str:
        return self._base64

    # Retorna possíveis erros
    def get_errors(self) -> str:
        return self._message_error
