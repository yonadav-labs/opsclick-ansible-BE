FROM python:latest

RUN echo 'Acquire::http { Proxy "http://172.17.0.2:3142"; };' >> /etc/apt/apt.conf.d/01proxy
RUN apt-get update && apt-get -y upgrade

RUN mkdir /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt -i "http://172.17.0.2:3141/root/pypi/" --trusted-host 172.17.0.2
COPY ./django-mongoengine /tmp

RUN adduser --disabled-password --gecos '' apiuser

RUN pip install -e /tmp/

