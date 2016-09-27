FROM python:latest

RUN echo 'Acquire::http { Proxy "http://172.17.0.2:3142"; };' >> /etc/apt/apt.conf.d/01proxy
RUN apt-get update && apt-get -y upgrade

RUN mkdir /code
COPY ./requirements.txt /code

WORKDIR /code
RUN pip install -r requirements.txt -i "http://172.17.0.2:3141/root/pypi/" --trusted-host 172.17.0.2

COPY ./django-mongoengine /tmp
RUN pip install -e /tmp/

