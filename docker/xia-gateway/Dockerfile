FROM xia-base

RUN apt-get -y install iputils-ping

RUN apt-get -y install ant openjdk-8-jdk

RUN apt-get -y install binutils-msp430 gcc-msp430 msp430mcu gcc-avr avr-libc msp430-libc

RUN git clone -b release-2-7 https://github.com/contiki-os/contiki.git 

COPY . ./

COPY xia-udp-gateway /xia-core/applications/examples/xia-udp-gateway

RUN /make-contiki

#ENTRYPOINT ["./init"]

