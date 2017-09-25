FROM xia-base

# Install Java to run Cooja
RUN apt-get -y install ant openjdk-8-jdk

# Install tools to build msp430 moto firmware
RUN apt-get -y install binutils-msp430 gcc-msp430 msp430mcu gcc-avr avr-libc msp430-libc

# Install wget to download IP list from the Border Router
RUN apt-get -y install wget

# Clone Contiki repository
RUN git clone -b release-2-7 https://github.com/contiki-os/contiki.git 

# Copy localdag workaround
COPY getlocaldag.c ./xia-core/applications/example/getlocaldag.c

# Copy Make file
COPY Makefile ./xia-core/applications/example/Makefile

# Copy build script
COPY make-gateway ./make-gateway

# Run build script 
RUN ./make-gateway

# Copy Cooja Project
COPY xia-ipv6-rpl-udp.csc ./xia-ipv6-rpl-udp.csc

# Copy gateway service
COPY xia-udp-gateway ./xia-core/applications/example/xia-udp-gateway

# Copy initialization Script
COPY init ./init

# Configure initialization script as entrypoint
ENTRYPOINT ["./init"]
