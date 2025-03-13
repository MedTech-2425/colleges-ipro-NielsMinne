import requests
import sys
import json

artist = input("Welke artiest wil je zien? ")
limit = input("Hoeveel liedjes wil je zien? ")
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={limit}&term={artist}")

# print(json.dumps(response.json(), indent=2))

songs = response.json()
for result in songs["results"]:
    print("Track name:", result["trackName"])