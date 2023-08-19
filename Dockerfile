# Use a imagem base do Python
FROM python:3.8

# Crie e navegue até o diretório do aplicativo
WORKDIR /app

# Copie o código do aplicativo para o contêiner
COPY . /app

# Instale as dependências
RUN pip install Flask Flask-SQLAlchemy

# Expõe a porta 5000 para acessar o aplicativo Flask
EXPOSE 5000

# Comando para iniciar o aplicativo
CMD ["python", "app.py"]
