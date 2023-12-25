#!/bin/sh

echo "DB not yet run..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
done

echo "DB did run."

python3 manage.py migrate --noinput --settings=config.debug

python3 manage.py runserver 0.0.0.0:8000 --settings=config.debug
