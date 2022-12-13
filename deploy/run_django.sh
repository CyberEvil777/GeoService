#!/bin/sh

python "manage.py" migrate --noinput

python "manage.py" parse_csv --noinput
