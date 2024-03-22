FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Встановлюємо the working directory in the container
WORKDIR /src

# contents of the src/ directory into the container
COPY src/ .

# .env file into the container
COPY .env /src

RUN pip install --no-cache-dir -r requirements.txt

#  additional setup steps, optionally
# RUN addgroup --system django && adduser --system django --ingroup django
# USER django