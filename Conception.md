# Conception

Theory of this app.

## Table of contents
* [Install](#install)
* [Database](#database)
* [Architecture](#architecture)
* [Pages](#pages)
* [API](#api)
* [Unit tests](#unit-tests)

## Install

### Production mode

```bash
git clone https://github.com/light-hat/firefly
cd firefly/src
docker-compose up -d --build
```

### Debug mode

This mode uses for debugging and development if you need a docker. 

```bash
cd firefly/src
docker-compose -f docker-compose-debug.yml up -d --build
```

### Dockerless develop mode

This mode uses for development.

Create venv and install requirements:

```bash
cd firefly/src/firefly
python3 -m venv venv
pip3 install -r requirements.txt
```

Activate it:

```bash
# Linux
source venv/bin/activate
```

```powershell
# Windows
.\venv\Scripts\activate
```

Make migrations to DB and run server

```bash
python3 manage.py migrate
python3 manage.py runserver --settings=config.develop
```

## Database
...

## Architecture
...

## Pages
...

## API
...

## Unit tests
...
