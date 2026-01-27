import os
import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
vehicle = "car"
key = os.getenv("GRAPHOPPER_KEY")

def geocoding(location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({
        "q": location,
        "limit": "1",
        "key": key
    })

    replydata = requests.get(url, timeout=10)
    json_data = replydata.json()
    json_status = replydata.status_code

    print("Geocoding API URL for " + location + ":\n" + url)

    if json_status == 200 and json_data.get("hits"):
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
    else:
        lat = None
        lng = None

    return json_status, lat, lng


def routing(lat1, lng1, lat2, lng2, vehicle, key):
    params = [
        ("key", key),
        ("vehicle", vehicle),
        ("point", f"{lat1},{lng1}"),
        ("point", f"{lat2},{lng2}"),
        ("points_encoded", "false"),
    ]
    url = route_url + urllib.parse.urlencode(params)

    reply = requests.get(url, timeout=10)
    data = reply.json()

    print("=================================================")
    print("Routing API Status:", reply.status_code)
    print("Routing API URL:\n" + url)
    print("=================================================")

    if reply.status_code != 200:
        print("Routing error:", data)
        return None

    path = data["paths"][0]
    distance_km = path["distance"] / 1000
    time_sec = path["time"] / 1000

    return distance_km, time_sec


# --- MAIN ---
if not key:
    print("ERROR: GRAPHOPPER_KEY is not set.")
    print('Run first: export GRAPHOPPER_KEY="YOUR_API_KEY"')
    raise SystemExit(1)

s1, lat1, lng1 = geocoding(loc1, key)
s2, lat2, lng2 = geocoding(loc2, key)

if lat1 is None or lat2 is None:
    print("ERROR: Geocoding failed.")
    raise SystemExit(1)

result = routing(lat1, lng1, lat2, lng2, vehicle, key)
if result is None:
    raise SystemExit(1)

distance_km, time_sec = result
print(f"Distance: {distance_km:.1f} km")
print(f"Time: {time_sec/60:.1f} minutes")
