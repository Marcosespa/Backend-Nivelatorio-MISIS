# Usar una imagen base de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requisitos e instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . .

# Exponer el puerto en el que la aplicación Flask se ejecuta
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "run.py"]