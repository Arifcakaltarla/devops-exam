# Pf3 – Eigen Flask Microservice Experiment

## Doel
Een eigen Flask microservice bouwen en deployen als Docker container met JSON endpoints.

## Endpoints
- `GET /health` – status
- `GET /api/time` – UTC tijd (JSON)
- `POST /api/echo` – echo van JSON body
- `GET /api/joke` – haalt 1 joke op via JokeAPI (timeout + error handling)

## Bestanden
- `app/app.py`
- `app/requirements.txt`
- `Dockerfile`
- `screenshots/`

## Run (Docker)
```bash
docker build -t pf3-microservice .
docker rm -f pf3 2>/dev/null || true
docker run -d -p 5001:5001 --name pf3 pf3-microservice
```
## Test
curl -i http://localhost:5001/health
curl -i http://localhost:5001/api/time
curl -i -X POST -H "Content-Type: application/json" -d '{"msg":"hello"}' http://localhost:5001/api/echo
curl -i http://localhost:5001/api/joke

## Bewijs
screenshots/pf3_microservice_ok.png