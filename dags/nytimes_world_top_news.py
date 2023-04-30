import datetime
import requests
import json
from google.cloud import storage


def extract_world_top_news():

    url = "https://api.nytimes.com/svc/topstories/v2/world.json?api-key=YOUR_KEY"
    world_top_news_list = {'world_top_news_list': list()}
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

        world_top_news_list['world_top_news_list'].append(infos)

    bucket_name = "airflow-api-backups"
    bucket = storage.Client().get_bucket(bucket_name)
    
    blob = bucket.blob("world_top_news/world_top_news_file_" + datetime_now.strftime("%d_%m_%Y") + ".json")
    print(f"Salvando arquivo em: {bucket_name}/world_top_news")
    blob.upload_from_string(data=json.dumps(
        world_top_news_list), content_type='application/json')
