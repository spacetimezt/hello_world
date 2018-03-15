FROM ubuntu:16.04
MAINTAINER kira "dark_alex916@sina.com"
RUN apt-get update
RUN apt-get install -y python-dev python-pip libncurses5-dev git
RUN git clone https://github.com/w3h/isf.git /home/isf
RUN pip install --upgrade pip
RUN pip install gnureadline
RUN pip install pycrypto
RUN pip install butterfly