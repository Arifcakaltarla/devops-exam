import os
import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = os.getenv("GRAPHOPPER_KEY")


def km_to_miles(km):
    return km * 0.621371


def format_duration(seconds):
    seconds = int(seconds)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def geocoding(location, api_key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({
        "q": location,
        "limit": "1",
        "key": api_key
    })

    reply = requests.get(url, timeout=10)
    data = reply.json()

    # Extra info tonen zoals in het lab (location type)
    loc_type = ""
    if reply.status_code == 200 and data.get("hits"):
        hit = data["hits"][0]
        name = hit.get("name", "")
        state = hit.get("state", "")
        country = hit.get("country", "")
        osm_value = hit.get("osm_value", "")
        loc_type = f"{name}, {state}, {country} (Location Type: {osm_value})"

    print("Geocoding API URL for " + (loc_type if loc_type else location) + ":\n" + url)

    if reply.status_code == 200 and data.get("hits"):
        lat = data["hits"][0]["point"]["lat"]
        lng = data["hits"][0]["point"]["lng"]
        return reply.status_code, lat, lng, loc_type

    return reply.status_code, None, None, location


def routing(lat1, lng1, lat2, lng2, vehicle, api_key):
    params = [
        ("key", api_key),
        ("vehicle", vehicle),
        ("point", f"{lat1},{lng1}"),
        ("point", f"{lat2},{lng2}"),
        ("points_encoded", "false"),
        ("instructions", "true"),
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

    return data


def ask_vehicle():
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("Vehicle profiles available on Graphhopper:")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("car, bike, foot")
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    v = input("Enter a vehicle profile from the list above: ").strip().lower()
    if v not in ["car", "bike", "foot"]:
        print("Invalid vehicle. Defaulting to car.")
        v = "car"
    return v


# --- MAIN ---
if not key:
    print("ERROR: GRAPHOPPER_KEY is not set.")
    print('Run first: export GRAPHOPPER_KEY="YOUR_API_KEY"')
    raise SystemExit(1)

vehicle = ask_vehicle()
loc1 = input("Starting Location: ").strip()
loc2 = input("Destination: ").strip()

s1, lat1, lng1, loc1_info = geocoding(loc1, key)
s2, lat2, lng2, loc2_info = geocoding(loc2, key)

if lat1 is None or lat2 is None:
    print("ERROR: Geocoding failed.")
    raise SystemExit(1)

data = routing(lat1, lng1, lat2, lng2, vehicle, key)
if data is None:
    raise SystemExit(1)

path = data["paths"][0]
distance_km = path["distance"] / 1000
time_sec = path["time"] / 1000

print("=================================================")
print(f"Directions from {loc1_info} to {loc2_info} by {vehicle}")
print("=================================================")
print(f"Distance Traveled: {km_to_miles(distance_km):.1f} miles / {distance_km:.1f} km")
print(f"Trip Duration: {format_duration(time_sec)}")
print("=================================================")

instructions = path.get("instructions", [])
for step in instructions:
    text = step.get("text", "")
    dist_km = step.get("distance", 0) / 1000
    dist_mi = km_to_miles(dist_km)
    print(f"{text} ( {dist_km:.1f} km / {dist_mi:.1f} miles )")
