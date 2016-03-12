#!/bin/bash

set -x

if [ -z "$VCAP_APP_PORT" ];

then SERVER_PORT=5000;

else SERVER_PORT="$VCAP_APP_PORT";

fi

pip install --upgrade pip
pip install newspaper3k&

echo [$0] port is------------------- $SERVER_PORT

echo [$0] Starting Django Server...

python manage.py runserver --noreload 0.0.0.0:$SERVER_PORT
