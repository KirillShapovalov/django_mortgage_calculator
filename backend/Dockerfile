# pull official base image
FROM python:3.9-alpine
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
COPY poetry.lock pyproject.toml /usr/src/app/
RUN pip3 install poetry
RUN apk update && apk upgrade \
    && apk add gcc g++ libffi-dev openssl-dev python3-dev py3-setuptools jpeg-dev zlib-dev
RUN poetry install
# copy project
COPY . /usr/src/app