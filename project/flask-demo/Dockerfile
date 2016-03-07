FROM ubuntu:14.04.3

MAINTAINER Qi Liang <sfoolish.liang@gmail.com>

RUN apt-get update && apt-get install -y \
	 curl \
	 python-dev \
	 python-pip \
	 wget \
	 vim

COPY yardstick/ssh /root/.ssh
COPY app /var/www/app
RUN pip install -r /var/www/app/requirements.txt

EXPOSE 5000

CMD ["python", "/var/www/app/main.py"]
