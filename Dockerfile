FROM python:3.13.0a4-alpine

RUN apk update && apk add --no-cache git util-linux

RUN pip install --no-cache-dir -U checkov

ENTRYPOINT ["checkov"]
