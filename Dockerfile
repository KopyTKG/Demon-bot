FROM python:3.9.7-buster

LABEL maintainer="https://github.com/KopyTKG"

RUN apt-get update

WORKDIR /usr/local/sbin

COPY . .

RUN pip install -r requirements.txt

RUN apt install ffmpeg -y

CMD ["python", "./main.py"]