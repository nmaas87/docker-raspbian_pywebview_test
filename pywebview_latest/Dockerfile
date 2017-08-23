FROM nmaas87/docker-raspbian_xinit_test:latest_opt2
MAINTAINER Nico Maas <mail@nico-maas.de>
ENV DEBIAN_FRONTEND noninteractive
RUN [ "cross-build-start" ]

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
        python3-pip python3-pyqt5 python-gi gir1.2-webkit-3.0=2.4.9-1~deb8u1+rpi1 gir1.2-javascriptcoregtk-3.0=2.4.9-1~deb8u1+rpi1 libjavascriptcoregtk-3.0-0=2.4.9-1~deb8u1+rpi1 libwebkitgtk-3.0-0=2.4.9-1~deb8u1+rpi1 \
    && apt-get autoremove -qqy \
    && apt-get autoclean -y \
    && apt-get clean && rm -rf /var/lib/apt/lists/* && mkdir /var/lib/apt/lists/partial \
    && pip3 install Flask pywebview \
    && mkdir /usr/src/app/templates /usr/src/app/static

# copy program
COPY src /usr/src/app

# start init system
ENV INITSYSTEM on

RUN [ "cross-build-end" ]  
