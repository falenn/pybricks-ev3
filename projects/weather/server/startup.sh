#!/bin/bash

# run where you want these set up
WORKING_DIR=$PWD

docker-compose down
docker rm server_mosquitto_1
docker volume rm mosquitto-config

mkdir $WORKING_DIR/mosquitto-config
mkdir $WORKING_DIR/mosquitto-data
mkdir $WORKING_DIR/mosquitto-log


docker volume create -d local -o type=none -o o=bind -o device=$WORKING_DIR/mosquitto-config mosquitto-config
docker volume create -d local -o type=none -o o=bind -o device=$WORKING_DIR/mosquitto-data mosquitto-data
docker volume create -d local -o type=none -o o=bind -o device=$WORKING_DIR/mosquitto-log mosquitto-log

#touch $WORKING_DIR/mosquitto-data/_data
#touch $WORKING_DIR/mosquitto-log/_data
#touch $WORKING_DIR/mosquitto-log/mosquitto.log
#touch $WORKING_DIR/mosquitto-config/_data

sudo chown -R 1001:1001 $WORKING_DIR/mosquitto-data
sudo chown -R 1001:1001 $WORKING_DIR/mosquitto-log
sudo chown -R 1001:1001 $WORKING_DIR/mosquitto-config

sudo chmod -R ugo+rwx $WORKING_DIR/mosquitto-data
sudo chmod -R ugo+rwx $WORKING_DIR/mosquitto-log
sudo chmod -R ugo+rwx $WORKING_DIR/mosquitto-config

# config heredoc for mosquitto.conf
cat > $WORKING_DIR/mosquitto-config/mosquitto.conf << EOF
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
listener 1883
bind_interface eth0
allow_anonymous true
EOF

# create password file / robots:robots
cat > $WORKING_DIR/mosquitto-config/pwdfile << EOF
robots:$7$101$TdwP4Y1uJ+tFo9Bn$84rK4XGZEuBmuKJHABOT4pQOzQQPX2LIhN/m/kLG6OgxT+vS8w6vCofgzd7YonvcKXTGIwK5tFe6nAWLpCT4Ow==
EOF


# start mosquitto
docker-compose up 
