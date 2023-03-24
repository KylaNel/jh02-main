FROM ubuntu:latest

# Install relevant pakages
RUN apt-get update && \
    apt-get install -y unzip

# Fetch the Maputnik CLI from github and unzip it
ADD https://github.com/maputnik/editor/releases/download/v1.7.0/maputnik-linux.zip /.
RUN unzip maputnik-linux.zip

# Add the default style
ADD ./styles/style.json /.
ADD map.mbtiles /.
ADD config.json /.

# Add the run shell script
ADD ./run.sh /.
RUN chmod +x ./run.sh

# Change linux permission to run maputnik executable
RUN chmod +x maputnik

CMD /run.sh