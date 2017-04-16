FROM ubuntu:latest

RUN apt-get -y update && apt-get install -y git libxml2 libxml2-dev libssl-dev libprotobuf-dev protobuf-compiler python-protobuf python-networkx python-nacl python-pip python-tk python-dev python-requests python-crypto build-essential openssl swig ant openjdk-8-jdk net-tools \
 \
&& cd ~ \
&& git clone https://github.com/XIA-Project/xia-core.git \
&& cd xia-core \
&& git checkout xia-v2 \
&& ./configure \
&& make \
&& make clean \
&& export PATH=$PATH:~/xia-core/bin \
 \
&& apt-get install -y doxygen help2man python-sphinx \
&& make doc \
&& export MANPATH=$MANPATH:~/xia-core/doc/man \
 \
&& apt-get install -y python-twisted \
 \
&& cd ~ \
&& git clone https://github.com/contiki-os/contiki.git \
&& cd contiki \
&& git submodule update --init \
&& export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8


