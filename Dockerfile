# Usa uma imagem leve do Python
FROM python:3.12-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o requirements.txt e instala dependências do sistema
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    firebird-dev \
 && pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get remove -y gcc \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/*

# Copia o restante do código da aplicação para o container
COPY . .

# Expõe a porta padrão do Uvicorn/FastAPI
EXPOSE 8000

# Comando padrão para executar a aplicação FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
