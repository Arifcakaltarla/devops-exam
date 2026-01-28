from flask import Flask, jsonify, request
import datetime
import requests

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/api/time")
def get_time():
    now = datetime.datetime.utcnow().isoformat() + "Z"
    return jsonify(utc=now)

@app.post("/api/echo")
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(received=data)

@app.get("/api/joke")
def joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        j = r.json()
        return jsonify(joke=j.get("joke", "No joke field"), source="JokeAPI")
    except requests.RequestException as e:
        return jsonify(error="JokeAPI request failed", details=str(e)), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, threaded=False)

