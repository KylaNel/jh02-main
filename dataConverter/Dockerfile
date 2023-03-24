# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential liblua5.1-0 liblua5.1-0-dev libprotobuf-dev libsqlite3-dev protobuf-compiler shapelib libshp-dev libboost-program-options-dev libboost-filesystem-dev libboost-system-dev libboost-iostreams-dev rapidjson-dev git ca-certificates

RUN git clone https://github.com/systemed/tilemaker.git && \
    cd tilemaker && \  
# RUN cd /python-docker/tilemaker && \
    make && \
    make install && \
    # clean up, remove build-time only dependencies
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove build-essential liblua5.1-0-dev git

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]