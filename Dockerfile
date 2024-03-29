FROM            python:3.6-onbuild
MAINTAINER      a828215362@gmail.com

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools 

RUN mkdir -p /usr/src/app /etc/supervisor/conf.d /var/log/supervisord

WORKDIR /usr/src/app

ENV LANG en_US.UTF-8

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /

COPY ./docker/supervisor/supervisord.conf /etc/
COPY ./docker/supervisor/supervisor-uwsgi.conf /etc/supervisor/conf.d/  

RUN  chmod +x /entrypoint.sh