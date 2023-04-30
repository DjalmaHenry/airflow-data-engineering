from airflow import DAG
from datetime import datetime
from nytimes_realtime_news_feed import extract_realtime_news_feed
from nytimes_world_top_news import extract_world_top_news
from nytimes_movie_reviews import extract_movie_reviews
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "djalmahenry",
    "start_date": datetime(2023, 4, 30),
}

dag = DAG(
    "nytimes_backup",
    default_args=default_args,
    schedule_interval="20 12 * * 2",
    max_active_runs=1,
)

start_pipeline = DummyOperator(
    task_id="start_pipeline",
    dag=dag
)

extract_realtime_news_feed = PythonOperator(
    task_id='extract_realtime_news_feed',
    python_callable=extract_realtime_news_feed,
    dag=dag
)

extract_world_top_news = PythonOperator(
    task_id='extract_world_top_news',
    python_callable=extract_world_top_news,
    dag=dag
)

extract_movie_reviews = PythonOperator(
    task_id='extract_movie_reviews',
    python_callable=extract_movie_reviews,
    dag=dag
)

done_pipeline = DummyOperator(
    task_id="done_pipeline",
    dag=dag
)

start_pipeline >> [extract_realtime_news_feed, extract_world_top_news, extract_movie_reviews] >> done_pipeline
