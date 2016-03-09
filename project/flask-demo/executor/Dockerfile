FROM ubuntu:14.04.3

MAINTAINER Qi Liang <sfoolish.liang@gmail.com>

RUN apt-get update && apt-get install -y \
	 curl \
	 python-dev \
	 python-pip \
	 wget \
	 vim

COPY ./ssh /var/www/app/.ssh
COPY ./ /var/www/app
RUN pip install -r /var/www/app/requirements.txt

ENV HOME /var/www/app
WORKDIR /var/www/app

CMD ["celery", "worker", "-A", "main.celery", "--loglevel=info"]
