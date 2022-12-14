#!/bin/sh

python "manage.py" collectstatic --noinput

python "manage.py" migrate --noinput

python "manage.py" parse_csv

gunicorn -c "$GUNICORN_CONF" geoservice.wsgi:application
