FROM python:3

WORKDIR /habbits_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
