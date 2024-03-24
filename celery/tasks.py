from celery import shared_task

from src.scrape_to_postgres import scrape_ibrd


@shared_task
def scrape_to_postgres():
    scrape_ibrd()