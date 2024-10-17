# Define la imagen base que se utilizará para construir el contenedor. En este caso, es la imagen oficial de Python 3.12.7, que está basada en Debian/Ubuntu.
FROM python:3.12.7

# Establece el directorio de trabajo dentro del contenedor como /app.
WORKDIR /app 

# Copia el archivo requirements.txt desde tu máquina local (directorio de origen del proyecto) al directorio de trabajo dentro del contenedor (/app).
COPY requirements.txt . 

# Ejecuta el comando pip para instalar las dependencias listadas en requirements.txt.
# La opción --no-cache-dir evita que pip almacene archivos de instalación en caché, lo que reduce el tamaño de la imagen.
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

# Copia todo el contenido del directorio actual en tu máquina local (donde está el Dockerfile) al directorio de trabajo dentro del contenedor (/app).
COPY . . 

# Indica que el contenedor expondrá el puerto 8000.
EXPOSE 8000

# Define el comando por defecto que se ejecutará cuando el contenedor se inicie
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
