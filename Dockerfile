FROM python:3.10.10-slim-buster

EXPOSE 8000

ENV PYTHONPATH="${PYTHONPATH}:/app"
RUN mkdir /app
WORKDIR /app

RUN pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry install -n

COPY app /app/app
ENTRYPOINT poetry run uvicorn app.main:app --workers 3 --host 0.0.0.0 --timeout-keep-alive 60
