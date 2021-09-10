FROM python:3.8-slim-buster

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code
