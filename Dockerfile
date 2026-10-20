FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Dépendances d'abord : meilleur cache de build.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY main.py config.json ./

RUN mkdir -p /app/data
VOLUME ["/app/data"]

EXPOSE 8000

# Le dashboard doit écouter sur 0.0.0.0 dans un conteneur.
CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "8000", "--no-browser"]
