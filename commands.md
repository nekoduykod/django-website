# other commands
## very beginning - creates necessary files
django-admin startproject your_title

## creation of a new app
py manage.py startapp your_app

## when new app created (e.g. /projects..)
py manage.py migrate

## creates a model (check migrations/)
py manage.py makemigrations myapp
## when db in settings.py, use this, but no data will be
python manage.py makemigrations  > creates a table schema to be migrated to db
py manage.py migrate             > creates a table in your postgresql db

## create superuser for django.admin
py manage.py createsuperuser (sasha, password456, fake@gmail.com) <= or change via UI of Django admin UI