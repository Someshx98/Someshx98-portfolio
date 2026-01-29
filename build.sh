#!/usr/bin/env bash
set -o errexit

pip install --no-cache-dir -r requirements.txt

python manage.py collectstatic --no-input --clear
python manage.py migrate
python manage.py createadmin