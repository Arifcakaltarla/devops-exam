# Di1 – Lab 6.2.7: Build a Sample Web App in a Docker Container

## Doel
Een eenvoudige Python Flask webapp bouwen, containerizen met Docker en verifiëren via de command line.

## Context
Dit experiment is gebaseerd op **Cisco NetAcad – Lab 6.2.7** en toont:
- basis bash scripting
- een eenvoudige Flask webapp
- het bouwen en runnen van een Docker image en container

## Inhoud
- `user-input` : bash script (user input demo)
- `sample_app.py` : Flask webapp
- `templates/index.html` : HTML template
- `static/style.css` : CSS styling
- `run.sh` : automatiseert Dockerfile, build image en run container
- `screenshots/` : bewijs van uitvoering

## Uitvoering

### Bash script
```bash
chmod a+x user-input
./user-input
```

## Lokale Flask test
pip3 install flask
python3 sample_app.py
curl http://0.0.0.0:8080

## Docker build & run
chmod +x run.sh
./run.sh

## Verificatie
docker ps
curl http://localhost:8080

## Resultaat

Docker image: di1-sample-app

Docker container: di1-sample-container

Webapp bereikbaar via http://localhost:8080

Opmerking

Voor compatibiliteit met de DEVASC VM draait de Flask app zonder threading (threaded=False).

## Bewijs

Zie map screenshots/:

di1_user_input_ok.png

di1_flask_local_curl_ok.png

di1_docker_runsh_ok.png

di1_docker_ps_ok.png