import requests
import urllib.parse
import os

route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
key = os.getenv("GRAPHOPPER_KEY")

def geocoding(location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    print("Geocoding API URL for " + location + ":\n" + url)

    if json_status == 200:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
    else:
        lat = "null"
        lng = "null"

    return json_status, lat, lng

orig = geocoding(loc1, key)
print(orig)

dest = geocoding(loc2, key)
print(dest)
