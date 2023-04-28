import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/"
pokemon_list = list()

counter = 1

while url != None:
    payload={}
    headers = {}
    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
    url = response["next"]

    for item in response["results"]:
        pokemon_name = item["name"]
        url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response_pokemon = json.loads(requests.request("GET", url_pokemon, headers=headers, data=payload).text)

        infos = {
            "name": pokemon_name,
            "id": response_pokemon["id"],
            "height": response_pokemon["height"],
            "weight": response_pokemon["weight"],
            "is_default": response_pokemon["is_default"]
        }

        pokemon_list.append(infos)
        print(response_pokemon["id"])

    file_path = fr"/Users/djalmahenrique/Documents/GitHub/airflow-data-engineering/pokemon_files/pokemon_file_{counter}.json"

    with open(file_path, 'w') as outfile:
        print("Salvando arquivo em: ", file_path)
        json.dump(pokemon_list, outfile)

    outfile.close()
    counter = counter + 1
    pokemon_list = list()

print(pokemon_list)

