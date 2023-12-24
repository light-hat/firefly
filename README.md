<div align="center">
<h1>Firefly</h1>

Self-hosted file hosting.

[![Check](https://github.com/light-hat/firefly/actions/workflows/commit.yml/badge.svg)](https://github.com/light-hat/firefly/actions/workflows/commit.yml/)
[![GitHub release](https://img.shields.io/github/v/release/light-hat/firefly.svg)](https://GitHub.com/light-hat/firefly/releases/)

</div>

## Quickstart

```bash
git clone https://github.com/light-hat/firefly
cd firefly/src
docker-compose up -d --build
```

## Dockerless start

```bash
cd firefly/src/firefly
python3 -m venv venv
# Activate venv
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

Activate venv:

```bash
# Linux
source venv/bin/activate
```

```powershell
# Windows
.\venv\Scripts\activate
```

## Licensing

Firefly is licensed under the [MIT License](https://github.com/light-hat/firefly/blob/master/LICENSE).
