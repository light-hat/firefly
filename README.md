<div align="center">
<h1>Firefly</h1>

Self-hosted file hosting.

[![Check](https://github.com/light-hat/firefly/actions/workflows/commit.yml/badge.svg)](https://github.com/light-hat/firefly/actions/workflows/commit.yml/)
[![GitHub release](https://img.shields.io/github/v/release/light-hat/firefly.svg)](https://GitHub.com/light-hat/firefly/releases/)

</div>

## Quickstart

### Production

```bash
git clone https://github.com/light-hat/firefly
cd firefly/src
docker-compose up -d --build
```

### Debug

This mode uses for debugging and development if you need a docker. 

```bash
cd firefly/src
docker-compose -f docker-compose-debug.yml up -d --build
```

### Dockerless develop

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

## Licensing

Firefly is licensed under the [MIT License](https://github.com/light-hat/firefly/blob/master/LICENSE).
