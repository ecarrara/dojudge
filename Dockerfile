##
##  Python 2.7 (on Debian Wheezy)
##

FROM debian:wheezy
MAINTAINER Erle Carrara <carrara.erle@gmail.com>

ENV PYTHON_VERSION 2.7.8

# Install dependencies
RUN apt-get update && \
    apt-get install -y gcc \
    make \
    libbz2-dev \
    libsqlite3-dev \
    libreadline-dev \
    zlib1g-dev \
    libncurses5-dev \
    libssl-dev \
    libgdbm-dev

# Install Python 2.7.8
ADD https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tar.xz /tmp/
RUN cd /tmp && \
    tar xf Python-2.7.8.tar.xz && \
    cd /tmp/Python-2.7.8 && \
    ./configure --prefix=/usr \
                --enable-shared \
                --with-system-expat \
                --with-system-ffi \
                --enable-unicode=ucs4 && \
    make && \
    make install && \
    make clean && \
    rm -r /tmp/Python-2.7.8 /tmp/Python-2.7.8.tar.xz

# Install PIP
ADD https://bootstrap.pypa.io/get-pip.py /tmp/
RUN python /tmp/get-pip.py

ADD . /app
RUN pip install -r /app/requirements.txt

EXPOSE 9090

WORKDIR /app

CMD ["uwsgi", "--http", "0.0.0.0:9090", "-w", "deploy:app"]
