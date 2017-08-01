FROM xia-base

RUN apt-get -y install iputils-ping

RUN apt-get -y install ant openjdk-8-jdk

RUN apt-get -y install binutils-msp430 gcc-msp430 msp430mcu gcc-avr avr-libc msp430-libc

RUN apt-get -y install wget

RUN git clone -b release-2-7 https://github.com/contiki-os/contiki.git 

COPY getlocaldag.c ./xia-core/applications/example/getlocaldag.c

COPY Makefile ./xia-core/applications/example/Makefile

COPY make-gateway ./make-gateway

RUN ./make-gateway

COPY ipv6-rpl-udp.csc ./ipv6-rpl-udp.csc

COPY xia-udp-gateway ./xia-core/applications/example/xia-udp-gateway

COPY init ./init

ENTRYPOINT ["./init"]

