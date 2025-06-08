# Imagen obtenida de DockerHub
# https://github.com/docker-library/python/blob/059df87446003f462a05aed0cff9b884da0b6874/3.9/slim-bookworm/Dockerfile
FROM python:3.9-slim

# Defino el nombre de la carpeta de trabajo dentro del contenedor
WORKDIR /app

# Ruta del juego
COPY PiedraPapelTijera.py .

# Inicio el juego
CMD ["python", "PiedraPapelTijera.py"]