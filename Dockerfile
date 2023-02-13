FROM python:3.10.10-slim-buster

ENV PYTHONPATH="${PYTHONPATH}:/app"
RUN mkdir /app
WORKDIR /app

RUN pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry install -n
