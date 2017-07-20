FROM ubuntu:xenial

RUN apt-get update

RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

# Install required packages
RUN apt-get install -y git g++ make openssl libssl-dev
RUN apt-get install -y libprotobuf-dev protobuf-compiler
RUN apt-get install -y python-tk python-dev python-setuptools python-crypto python-requests
RUN apt-get install -y swig
RUN apt-get install -y python-argparse
RUN apt-get install -y python-pygame
RUN apt-get install -y libffi-dev python-crypto python-protobuf python-networkx python-pip
RUN apt-get install -y netcat
RUN apt-get install -y libxml2 libxml2-dev python-nacl build-essential
RUN apt-get install -y rsyslog

# tools
#RUN apt-get install -y vim tmux ack-grep curl socat netcat wget stunnel
RUN apt-get install -y net-tools

#RUN pip install --upgrade pip
#RUN pip install pynacl

COPY install-xia ./install-xia

RUN /install-xia

