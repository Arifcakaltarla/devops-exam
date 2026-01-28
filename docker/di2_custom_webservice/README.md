# Di2 – Custom Docker Image Experiment (Web Service)

## Doel
Een eigen (niet-lab) webservice bouwen als Docker image en runnen als container, inclusief verificatie met curl.

## Bestanden
- `app.py` : Flask webservice met endpoints `/` en `/health`
- `requirements.txt` : Python dependencies
- `Dockerfile` : build van de image
- `screenshots/` : bewijs

## Build & Run

### Image bouwen
```bash
docker build -t di2-webservice .
```
## Container starten
docker rm -f di2-webservice 2>/dev/null || true
docker run -d --name di2-webservice -p 5000:5000 di2-webservice

## Verificatie
docker ps | grep di2
curl -i http://localhost:5000/health
curl -i http://localhost:5000/

## Resultaat

Image: di2-webservice

Container: di2-webservice

Poort: 5000 → http://localhost:5000

/health geeft JSON: {"status":"ok"}

## Opmerking

Voor compatibiliteit met de DEVASC VM draait Flask zonder threading (threaded=False, use_reloader=False).

## Bewijs

Zie screenshots/:

di2_docker_ps_ok.png

di2_curl_health_ok.png