#!/bin/bash

# run where you want these set up
WORKING_DIR=$PWD

mkdir $WORKING_DIR/mosquitto-config
mkdir $WORKING_DIR/mosquitto-data
mkdir $WORKING_DIR/mosquitto-log

docker volume create -d local -o type=none -o o=bind -o device=$WORKING_DIR/mosquitto-config mosquitto-config
docker volume create -d local -o type=none -o o=bind -o device=$WORKING_DIR/mosquitto-data mosquitto-data
docker volume create -d local -o type=none -o o=bind -o device=$WORKING_DIR/mosquitto-log mosquitto-log

touch $WORKING_DIR/mosquitto-data/_data
touch $WORKING_DIR/mosquitto-log/_data
touch $WORKING_DIR/mosquitto-config/_data

# config heredoc for mosquitto.conf
cat > $WORKING_DIR/mosquitto-config/mosquitto.conf << EOF
persistence true
persistence_location /opt/mosquitto/data/
log_dest file /opt/mosquitto/log/mosquitto.log
EOF

docker-compose up
