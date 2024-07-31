#!/bin/bash -x

python manage.py showmigrations
python manage.py migrate --noinput
