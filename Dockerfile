FROM python:3.13-alpine

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root

COPY . .

CMD ["poetry", "run", "python", "src/__main__.py"]
