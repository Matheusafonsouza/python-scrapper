FROM python:3

# Cria a pasta do projeto /code
RUN mkdir /code

# Coloca o /code como diretório principal
WORKDIR /code

# Adiciona o requirements.txt na pasta code
ADD requirements.txt /code/

# Instala as dependencias do projeto no docker
RUN pip install -r requirements.txt

# Adicionar o código no /code/
ADD . /code/

# roda a aplicação
CMD ["python", "./app.py"]