FROM xia-base

COPY . ./

RUN apt-get -y install ant openjdk-8-jdk

RUN /get-contiki

ENTRYPOINT ["./init"]

