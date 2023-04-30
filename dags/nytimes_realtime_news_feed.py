import datetime
import requests
import json
from google.cloud import storage


def extract_realtime_news_feed():

    url = "https://api.nytimes.com/svc/news/v3/content/nyt/world.json?api-key=YOUR_KEY"
    realtime_news_feed_list = {'realtime_news_feed_list': list()}
    datetime_now = datetime.datetime.now() - datetime.timedelta(hours=3)

    payload = {}
    headers = {}
    response = json.loads(requests.request(
        "GET", url, headers=headers, data=payload).text)

    for item in response["results"]:
        infos = {
            "subsection": item["subsection"],
            "title": item["title"],
            "abstract": item["abstract"],
            "url": item["url"],
            "byline": item["byline"],
            "published_date": item["published_date"]
        }

        realtime_news_feed_list['realtime_news_feed_list'].append(infos)

    bucket_name = "airflow-api-backups"
    bucket = storage.Client().get_bucket(bucket_name)
    
    blob = bucket.blob("realtime_news_feed/realtime_news_feed_file_" + datetime_now.strftime("%d_%m_%Y") + ".json")
    print(f"Salvando arquivo em: {bucket_name}/realtime_news_feed")
    blob.upload_from_string(data=json.dumps(
        realtime_news_feed_list), content_type='application/json')
