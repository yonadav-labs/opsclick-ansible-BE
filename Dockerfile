FROM python:latest

RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y python-pip python-dev build-essential libssl-dev libffi-dev
RUN pip2 install --upgrade ansible dopy==0.3.5

RUN mkdir /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --upgrade -r requirements.txt 

COPY ./django-mongoengine /tmp/django-mongoengine
#COPY ./django-rest-framework-mongoengine /tmp/django-rest-framework-mongoengine

#RUN adduser --disabled-password --gecos '' apiuser

RUN pip install -e /tmp/django-mongoengine # /tmp/django-rest-framework-mongoengine

