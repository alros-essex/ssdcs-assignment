#!/bin/sh
while :; do
    sleep 60
    rm /var/log/filebeat/*
    /etc/init.d/filebeat restart
done