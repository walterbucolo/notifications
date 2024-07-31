FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade --no-cache-dir poetry

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY ./app /app
COPY ./bin /app/bin

RUN chmod +x ./bin/migrate.sh ./bin/run.sh

CMD ["sh", "-c", "./bin/migrate.sh && ./bin/run.sh"]
