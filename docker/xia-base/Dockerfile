FROM ubuntu:xenial

RUN apt-get update

# Prepare environment
RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update -y && \
 apt-get upgrade -y && \
 apt-get dist-upgrade -y && \
 apt-get install build-essential software-properties-common -y && \
 add-apt-repository ppa:ubuntu-toolchain-r/test -y && \
 apt-get update -y && \
 apt-get install gcc-7 g++-7 -y && \
 update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60 --slave /usr/bin/g++ g++ /usr/bin/g++-7 && \
 update-alternatives --config gcc

# Install required packages
RUN apt-get install -y git make openssl libssl-dev
RUN apt-get install -y libprotobuf-dev protobuf-compiler
RUN apt-get install -y python-tk python-dev python-setuptools python-crypto python-requests
RUN apt-get install -y swig
RUN apt-get install -y python-argparse
RUN apt-get install -y python-pygame
RUN apt-get install -y libffi-dev python-crypto python-protobuf python-networkx python-pip
RUN apt-get install -y netcat
RUN apt-get install -y libxml2 libxml2-dev python-nacl build-essential
RUN apt-get install -y rsyslog

# Install tools
RUN apt-get install -y net-tools
RUN apt-get install -y iputils-ping

# Copy XIA instalation Script
COPY install-xia ./install-xia

# Run XIA instalation Script
RUN /install-xia

# To run a reduced version of XIA with smaller XIDs (2 bytes) uncomment the following commands
#COPY clicknetxia.h /xia-core/api/include/clicknetxia.h

#COPY xia.h /xia-core/click/include/clicknet/xia.h

#COPY xip.h /xia-core/api/include/xip.h

# Copy XIA instalation Script
COPY build-xia ./build-xia

# Run XIA build Script
RUN /build-xia
