#!/bin/sh

# build nginx
cd containers/nginx/
docker build . -t custom_nginx
cd ../..

# build app
rm -fr containers/app/.static-tmp
cp -fr static containers/app/.static-tmp
cd containers/app
docker build . -t safe_repository
cd ../..

# start docker
docker-compose up
