#!/bin/sh

BUILD_NGINX=`false`
BUILD_APP=`true`

if $BUILD_NGINX
then
    cd containers/nginx/
    docker build . -t custom_nginx
    cd ../..
fi

if $BUILD_APP
then
    cd containers/app
    docker build . -t safe_repository
    cd ../..
fi

docker-compose up