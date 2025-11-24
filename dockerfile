# # base image
# FROM python:3.12-slim

# # set encirinment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # set work directory
# WORKDIR /app

# # install dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # install poetry
# RUN curl -sSL https://install.python-poetry.org | python3 -
# ENV PATH="/root/.local/bin:$PATH"

# # copy poetry files
# COPY pyproject.toml poetry.lock /app/

# # install project dependencies
# RUN poetry config virtualenvs.create false \
#     && poetry install --no-interaction --no-ansi --no-root

# # copy project files
# COPY . /app/

# # expose port
# EXPOSE 8000

# # run server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=Asia/Kathmandu
ENV PYTHONPATH=/app
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Install required system packages
RUN apk update && apk add --no-cache \
    tzdata make \
    gcc g++ musl-dev libffi-dev openssl-dev \
    curl cargo \
    python3-dev jpeg-dev zlib-dev rust \
    postgresql-dev \
    geos geos-dev \
    gdal gdal-dev \
    proj proj-dev \
    build-base openssh

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    poetry config virtualenvs.create false && \
    poetry config installer.max-workers 10

# Copy Poetry files
COPY pyproject.toml poetry.lock /app/

# Install Python dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy project AFTER dependencies (improves caching)
COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]