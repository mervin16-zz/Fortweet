FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y

RUN apt install software-properties-common -y

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt install python3.8 -y

RUN apt-get install -y python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["gunicorn", "--config", "gunicorn.py", "app:app"]