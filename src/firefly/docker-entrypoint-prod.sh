#!/bin/sh

echo "DB not yet run..."

sleep 2

echo "DB did run."

python3 manage.py collectstatic --noinput

python3 manage.py migrate --noinput

python3 manage.py runserver 0.0.0.0:8000
