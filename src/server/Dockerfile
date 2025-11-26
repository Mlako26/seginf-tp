FROM python:3.11-slim

# Evita problemas con buffering de logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código
COPY . .

# Exponer el puerto donde corre Flask
EXPOSE 8080

# Comando para lanzar el servidor
CMD ["python", "backend.py"]
