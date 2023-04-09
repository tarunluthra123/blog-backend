FROM python:3.9-slim

RUN pip install poetry

WORKDIR /app

RUN pip install gunicorn==20.1.0
RUN poetry config virtualenvs.create false
ADD pyproject.toml poetry.lock /app/
RUN poetry install --no-root --no-interaction --no-ansi


COPY . .

ENTRYPOINT [ "gunicorn", "blog.wsgi", "-b", "0.0.0.0:8000"]
