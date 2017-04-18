FROM ubuntu:latest

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

COPY . ./

RUN /install-packages.sh
RUN /get-xia.sh
RUN /build-xia.sh

