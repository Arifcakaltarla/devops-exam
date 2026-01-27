from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_CATEGORIES = "https://v2.jokeapi.dev/categories"
API_JOKE = "https://v2.jokeapi.dev/joke/"

def fetch_categories():
    try:
        r = requests.get(API_CATEGORIES, timeout=10)
        if r.status_code == 200:
            data = r.json()
            # JokeAPI returns categories in: data["categories"]
            return data.get("categories", [])
    except requests.RequestException:
        pass
    return []

def fetch_joke(category="Any"):
    try:
        url = API_JOKE + category
        r = requests.get(url, params={"safe-mode": ""}, timeout=10)

        if r.status_code != 200:
            return None, f"API error (status {r.status_code})"

        data = r.json()
        if data.get("error") is True:
            return None, "JokeAPI returned an error."

        if data.get("type") == "single":
            joke_text = data.get("joke", "")
        else:
            joke_text = f'{data.get("setup", "")} {data.get("delivery", "")}'

        return {
            "category": data.get("category"),
            "type": data.get("type"),
            "joke": joke_text
        }, None

    except requests.exceptions.Timeout:
        return None, "Timeout: API did not respond in time."
    except requests.RequestException as e:
        return None, f"Request error: {e}"
    except ValueError:
        return None, "Error: response is not valid JSON."

@app.route("/", methods=["GET", "POST"])
def index():
    categories = fetch_categories()
    selected = "Any"
    result = None
    error = None
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if request.method == "POST":
        selected = request.form.get("category", "Any")
        result, error = fetch_joke(selected)

    return render_template(
        "index.html",
        categories=categories,
        selected=selected,
        result=result,
        error=error,
        now=now
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
