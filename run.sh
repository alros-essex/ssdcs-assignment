#!/bin/sh

# build nginx
cd containers/nginx/
docker build . -t custom_nginx
cd ../..

# build mysql
cd containers/mysql
docker build . -t custom_mysql
cd ../..

# build app
rm -fr containers/app/.static-tmp
cp -R static containers/app/.static-tmp
cd containers/app
docker build . -t safe_repository
cd ../..



docker-compose up
