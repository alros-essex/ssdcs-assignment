#!/bin/sh

basedir=$PWD

if [ -n "$1" ] && [ "$1" = "--use-cached" ]; then
  use_cached="true"
else
  use_cached="false"
fi

# go to web-interface, compile static files for serving
cd "$basedir"/containers/web-interface || {
  echo "Could not cd into web-interface directory. Aborting run script"
  exit 1
}

if [ $use_cached = "false" ]; then
  echo "Installing angular packages..."
  rm -rf node_modules
  npm install
else
  echo "Using existing angular packages"
fi

ng build

# run flask app
cd "$basedir" || {
  echo "Could not cd into project base directory. Aborting run script"
  exit 1
}
python3 containers/app/main.py
