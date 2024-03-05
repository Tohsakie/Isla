FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY meteo.py .
COPY app.py .
COPY isla.h5 .
COPY gpt.py .


EXPOSE 8082

