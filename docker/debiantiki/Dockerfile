FROM debian

# Tools
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y bzip2 wget multiarch-support git-core make gcc

# Install doxygen
RUN apt-get install -y doxygen && doxygen --version

# Install msp430 toolchain
RUN apt-get install -y lib32z1
RUN wget http://adamdunkels.github.io/contiki-fork/mspgcc-4.7.0-compiled.tar.bz2 && \
    tar xjf mspgcc*.tar.bz2 -C /tmp/ && \
    cp -f -r /tmp/msp430/* /usr/local/ &&\
    rm -rf /tmp/msp430 mspgcc*.tar.bz2 && \
    msp430-gcc --version

# Install avr toolchain
RUN apt-get -qq install gcc-avr avr-libc

# Install 32-bit compatibility libraries
RUN apt-get -qq install \
  libc6:i386 \
  libgcc1:i386 \
  gcc-4.9-base:i386 \
  libstdc++5:i386 \
  libstdc++6:i386

# Install old APCS ARM toolchain for mc1233x and mbxxx
#RUN wget https://raw.githubusercontent.com/wiki/malvira/libmc1322x/files/arm-2008q3-66-arm-none-eabi-i686-pc-linux-gnu.tar.bz2 && \
#    tar xjf arm-2008q3*.tar.bz2 -C /tmp/ && \
#    cp -f -r /tmp/arm-2008q3/* /usr/ && \
#    rm -rf /tmp/arm-2008q3 arm-2008q3*.tar.bz2 && \
#    arm-none-eabi-gcc --version

# Install mainline ARM toolchain.
RUN apt-get -qq install \
  gcc-arm-none-eabi \
  srecord && \
  arm-none-eabi-gcc --version

# Install SDCC from a purpose-built bundle
RUN apt-get install -y lib32stdc++6
RUN wget https://raw.githubusercontent.com/wiki/g-oikonomou/contiki-sensinode/files/sdcc.tar.gz && \
    tar xzf sdcc.tar.gz -C /tmp/ && \
    cp -f -r /tmp/sdcc/* /usr/local/ && \
    rm -rf /tmp/sdcc sdcc.tar.gz && \
    sdcc --version

## Clone and build cc65 when testing 6502 ports
RUN git clone https://github.com/cc65/cc65 /tmp/cc65 && \
    make -C /tmp/cc65 bin apple2enh atarixl c64 c128 && \
    make -C /tmp/cc65 avail && \
    export CC65_HOME=/tmp/cc65/ && \
    cc65 --version

# Install RL78 GCC toolchain
RUN apt-get install -y libncurses5-dev
RUN apt-get install -y libncurses5:i386 zlib1g:i386
RUN wget http://adamdunkels.github.io/contiki-fork/gnurl78-v13.02-elf_1-2_i386.deb && \
    dpkg -i gnurl78*.deb

# Compile cooja.jar only when it's going to be needed
RUN apt-get install -y ant 
RUN apt-get install -y openjdk-7-jdk
ENV JAVA_HOME /usr/lib/jvm/default-java
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8
RUN git clone https://github.com/contiki-os/contiki

WORKDIR contiki
RUN git submodule update --init 
RUN ant -q -f tools/cooja/build.xml jar
