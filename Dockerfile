# Usa imagem base do Python com tamanho reduzido
FROM python:3.12-slim

# Define modo não interativo para evitar prompts durante instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instala bibliotecas de sistema necessárias e o Tesseract com idioma português
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    tesseract-ocr \
    tesseract-ocr-por \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1 \
    libmysqlclient-dev \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia todos os arquivos do projeto para o container
COPY . .

# Instala as dependências Python definidas no requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8082 (a que será usada pelo Uvicorn)
EXPOSE 8082

# Comando de inicialização do FastAPI com Uvicorn na porta 8082
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8082"]
