FROM python:3.11-slim-bullseye

LABEL maintainer="Daniel Ticona <ghostdanyt.a@gmail.com>"

WORKDIR /home/django/app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN addgroup --system django && adduser --system --ingroup django django && mkdir -p /home/django/app && chown -R django:django /home/django/app && \
    apt-get update && apt-get upgrade -y && \
    apt-get install -y gcc build-essential libssl-dev libffi-dev python3-dev zlib1g-dev libjpeg-dev libpq-dev libjbig0 liblcms2-2 libopenjp2-7 libtiff5 libwebp6 libwebpdemux2 libwebpmux3 && \
    apt-get clean

RUN pip install -U pip setuptools wheel && \
    rm -rf /var/lib/apt/lists/* /root/.cache /tmp/pip*

COPY requirements.txt .

COPY requirements.test.txt .

RUN pip install -r requirements.txt --default-timeout=1000 --no-cache-dir

RUN pip install -r requirements.test.txt --default-timeout=1000 --no-cache-dir

COPY . .

USER django

EXPOSE 8000
