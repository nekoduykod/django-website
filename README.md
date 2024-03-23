# Task
A simple Django application, containing one API endpoint, several models, scraper and scheduled task. 

Scraper should be run every day at 3am, scrape first 10 pages from IBRD ([The World Bank](https://projects.worldbank.org/en/projects-operations/projects-list?projectfinancialtype_exact=IBRD&os=0&sector_exact=Health)), parse them and write follow data to database:
- project_id,
- title,
- date,
- amount (amount of commitment),
- status,
- location,
- sector,
- type

Make an RESTAPI GET endpoint https://localhost:8000/projects, that provides transaction data using pagination (100 per request).
API endpoints must be cached with redis. Use docker for containerizing an application, Redis, db, etc... 

# Run locally
git clone https://github.com/nekoduykod/django_website_scrape

1) python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

2) create your .env from an example 
run python src\scrape_to_postgres.py

3) download Redis. Open redis-cli.exe. PING. redis-server

4) py manage.py runserver
Open https://localhost:8000/projects

# Run through Docker
git clone https://github.com/nekoduykod/django_website_scrape

create your .env from an example 

docker-compose up --build   // If detached mode, add -d flag

docker-compose down // if to stop, or via Docker Desktop UI

# Some pictures

<img src='1scraped_projects_django.jpg' />

<img src='2pagination.jpg' />

<img src='3redis_cache.jpg' />

<img src='4source_scraped.jpg' />