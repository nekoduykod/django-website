# other commands
## DJANGO
## very beginning - creates necessary files
django-admin startproject your_title
## creation of a new app
py manage.py startapp your_app
## when new app created (e.g. /projects..)
py manage.py migrate

## when db in settings.py, use this, but no data will be
python manage.py makemigrations myapp (or without/other apps)  => creates a table schema to be migrated to db
py manage.py migrate => creates a table in your postgresql db
## create superuser for django.admin
py manage.py createsuperuser (sasha, password456, fake@gmail.com) <= or change via UI of Django admin UI

## CELERY
##  starts the Celery worker, which listens for and executes tasks.
celery -A proj worker -l INFO
## for periodic tasks scheduled, to start the Celery beat scheduler.
celery -A proj beat -l INFO
## inspect active tasks
celery -A proj inspect active

## purge all tasks if needed
celery -A proj purge
##  if made changes to periodic tasks and need to reset them
celery -A proj beat -l INFO --purge