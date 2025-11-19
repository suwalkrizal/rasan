# base image
FROM python:3.12-slim

# set encirinment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# copy poetry files
COPY pyproject.toml poetry.lock /app/

# install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# copy project files
COPY . /app/

# expose port
EXPOSE 8000

# run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]