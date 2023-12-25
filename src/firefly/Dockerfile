FROM python:3.12-alpine3.19

RUN apk add --update-cache curl netcat-openbsd

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["sh", "./docker-entrypoint-prod.sh"]
