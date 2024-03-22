FROM python:3.11

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# working directory in the container
WORKDIR /celery

# Celery project files into the container
COPY celery/ /celery

# COPY .env /celery

# install requirements file
RUN pip install --no-cache-dir -r celery_requirements.txt

# Optionally, create a non-root user to improve security after installing the dependencies
# RUN useradd -ms /bin/bash celery_user
# USER celery_user