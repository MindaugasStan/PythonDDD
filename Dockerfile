ARG PYTHON_VERSION=3.12

################################################################################

FROM python:${PYTHON_VERSION}-slim AS builder

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application into the container
COPY . /app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080"]