# AP3 – JokeAPI (Python REST API Integration)

## Description
This assignment demonstrates the integration of an external public REST API
into a Python application.

The script connects to JokeAPI, retrieves JSON data, parses the response,
and prints a formatted result to the terminal.

This experiment was created as an **own API experiment (Python)** according
to the DevOps evaluation criteria.

## Used API
- JokeAPI
- Endpoint: https://v2.jokeapi.dev/joke/Any

## Functionality
- Sends an HTTP GET request to a public REST API
- Checks HTTP status codes
- Parses JSON responses
- Handles different joke types (`single` / `twopart`)
- Includes timeout handling
- Includes error handling
- Displays formatted output in the terminal

## File
- `jokeapi_random_joke.py`

## How to Run
```bash
python3 jokeapi_random_joke.py
