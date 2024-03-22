from datetime import datetime, timedelta

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'myapp',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

default_args = {
    'owner': 'myapp',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'ibrd_dag_scrape',
    default_args=default_args,
    description='A simple Airflow DAG',
    schedule_interval='0 3 * * *',  # кожен день о 3 ночі
    catchup=False,
) as dag:
    scrape_task = BashOperator(
        task_id='scrape_data',
        bash_command='python /src/myapp/services/ibrd_scrape_to_postgres.py',
    )