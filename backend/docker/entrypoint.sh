#!/bin/sh
  

# django startup
./manage.py migrate --noinput
./manage.py createsuperuser --no-input 2>1 >/dev/null

exec "$@"
