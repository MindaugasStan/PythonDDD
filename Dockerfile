ARG PYTHON_VERSION=3.12

# Stage 1: Builder
FROM python:${PYTHON_VERSION}-slim AS builder

WORKDIR /app

RUN apt-get update \
    && apt-get install -y \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app
RUN python -m venv --system-site-packages --without-pip /venv \
    && /venv/bin/python -m pip install --no-cache-dir -r requirements.txt

################################################################################

# Stage 2: Runtime (Python DDD)
FROM python:${PYTHON_VERSION}-slim as python-ddd

RUN apt-get update \
    && apt-get install -y \
        libpq5 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /venv /venv
ENV PATH=/venv/bin:$PATH

# Copy the application code
COPY . /app

EXPOSE 8080

# Default command to run the app (this can be overridden by docker-compose)
CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080" ]
