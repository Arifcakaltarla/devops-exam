import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
loc1 = "Washington, D.C."
key = "b6b52de4-6cc4-4dde-972b-46b22bbe561e"

url = geocode_url + urllib.parse.urlencode({"q": loc1, "limit": "1", "key": key})

reply = requests.get(url)
print(reply.json())
