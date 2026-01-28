# Pv2 – Python venv: Flask Deployment Experiment

## Doel
Een eigen Python virtual environment gebruiken om een Flask applicatie
te deployen.

## Context
Dit experiment toont een praktische toepassing van Python venv waarbij
een webapplicatie uitsluitend binnen de virtual environment draait.

## Gebruikte technologieën
- Python venv
- Flask
- Ubuntu (DEVASC VM)

## Bestanden
- `venv/` – Python virtual environment
- `app.py` – Flask applicatie
- `screenshots/` – visueel bewijs

## Uitvoering
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
python app.py
```
## Resultaat

Flask applicatie draait binnen een virtual environment

Webapp bereikbaar via http://127.0.0.1:5000

## Bewijs

In de map screenshots/ is een afbeelding toegevoegd als bewijs van de
werkende Flask applicatie binnen de venv.

## Besluit

Dit experiment toont hoe Python venv gebruikt kan worden voor het
isoleren en deployen van applicaties.