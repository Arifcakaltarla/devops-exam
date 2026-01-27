import requests
from datetime import datetime

API_URL = "https://v2.jokeapi.dev/joke/Any"

def get_random_joke():
    try:
        r = requests.get(API_URL, timeout=10)
        status = r.status_code

        if status != 200:
            print(f"API error - status code: {status}")
            print("Response:", r.text)
            return

        data = r.json()

        if data.get("error") is True:
            print("JokeAPI returned an error")
            return

        joke_type = data.get("type")
        category = data.get("category", "unknown")

        if joke_type == "single":
            joke_text = data.get("joke")
        else:
            joke_text = f'{data.get("setup")} {data.get("delivery")}'

        print("===================================")
        print("JokeAPI - Random Joke")
        print("===================================")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Status: {status}")
        print(f"Category: {category}")
        print(f"Type: {joke_type}")
        print("-----------------------------------")
        print(joke_text)
        print("===================================")

    except requests.exceptions.Timeout:
        print("Timeout: the API did not respond in time.")
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
    except ValueError:
        print("Error: response is not valid JSON.")

if __name__ == "__main__":
    get_random_joke()
