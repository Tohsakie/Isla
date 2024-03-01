FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY meteo.py .
COPY app.py .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8082

