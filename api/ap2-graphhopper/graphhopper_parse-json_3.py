import os
import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
key = os.getenv("GRAPHOPPER_KEY")


def geocoding(location: str, api_key: str):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": api_key})

    reply = requests.get(url, timeout=10)
    data = reply.json()

    print("Geocoding API URL for " + location + ":\n" + url)

    if reply.status_code == 200 and data.get("hits"):
        lat = data["hits"][0]["point"]["lat"]
        lng = data["hits"][0]["point"]["lng"]
        return reply.status_code, lat, lng
    return reply.status_code, None, None


def route(lat1: float, lng1: float, lat2: float, lng2: float, api_key: str):
    # Graphhopper expects points as: point=lat,lng (can be multiple point params)
    params = [
        ("point", f"{lat1},{lng1}"),
        ("point", f"{lat2},{lng2}"),
        ("vehicle", "car"),
        ("points_encoded", "false"),
        ("key", api_key),
    ]

    url = route_url + urllib.parse.urlencode(params)

    reply = requests.get(url, timeout=10)
    data = reply.json()

    print("Routing API URL:\n" + url)

    if reply.status_code != 200:
        # Graphhopper returns useful error messages in JSON
        print("Routing error:", data)
        return

    # Parse distance (meters) and time (ms)
    path = data["paths"][0]
    distance_m = path["distance"]
    time_ms = path["time"]

    distance_km = distance_m / 1000
    time_min = time_ms / 1000 / 60

    print(f"Distance: {distance_km:.2f} km")
    print(f"Time: {time_min:.1f} minutes")


# 1) Geocode both locations
status1, lat1, lng1 = geocoding(loc1, key)
status2, lat2, lng2 = geocoding(loc2, key)

print("Origin:", status1, lat1, lng1)
print("Dest:", status2, lat2, lng2)

# 2) Route if geocoding worked
if lat1 is not None and lat2 is not None:
    route(lat1, lng1, lat2, lng2, key)
else:
    print("Cannot route: geocoding failed.")
