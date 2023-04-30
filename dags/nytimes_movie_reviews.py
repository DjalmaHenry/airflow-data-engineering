import datetime
import requests
import json
from google.cloud import storage


def extract_movie_reviews():

    url = "https://api.nytimes.com/svc/movies/v2/reviews/all.json?api-key=YOUR_KEY"
    movie_reviews_list = {'movie_reviews_list': list()}
    datetime_now = datetime.datetime.now() - datetime.timedelta(hours=3)

    payload = {}
    headers = {}
    response = json.loads(requests.request(
        "GET", url, headers=headers, data=payload).text)

    for item in response["results"]:
        infos = {
            "display_title": item["display_title"],
            "summary_short": item["summary_short"],
            "publication_date": item["publication_date"],
            "link": item["link"]
        }

        movie_reviews_list['movie_reviews_list'].append(infos)

    bucket_name = "airflow-api-backups"
    bucket = storage.Client().get_bucket(bucket_name)
    
    blob = bucket.blob("movie_reviews/movie_reviews_file_" + datetime_now.strftime("%d_%m_%Y") + ".json")
    print(f"Salvando arquivo em: {bucket_name}/movie_reviews")
    blob.upload_from_string(data=json.dumps(
        movie_reviews_list), content_type='application/json')
