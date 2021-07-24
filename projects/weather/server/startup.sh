#!/bin/bash

# run where you want these set up
WORKING_DIR=$PWD

mkdir $WORKING_DIR/mosquitto-config
mkdir $WORKING_DIR/mosquitto-data
mkdir $WORKING_DIR/mosquitto-log

docker volume create -d local -o type=none -o bind -o device=$WORKING_DIR/config mosquitto-config
docker volume create -d local -o type=none -o bind -o device=$WORKING_DIR/data mosquitto-data
docker volume create -d local -o type=none -o bind -o device=$WORKING_DIR/log mosquitto-log

# config heredoc for mosquitto.conf
cat > $WORKING_DIR/config/mosquitto.conf << EOF
persistence true
persistence_location /opt/mosquitto/data/
log_dest file /opt/mosquitto/log/mosquitto.log
EOF

docker-compose up