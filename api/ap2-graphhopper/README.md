# AP2 – Graphhopper Directions API

## Doel
Integreren van een externe REST API (Graphhopper) in een Python applicatie.
De applicatie:
- vraagt locaties en voertuigtype
- gebruikt Geocoding + Routing API
- verwerkt JSON responses
- toont afstand, duur en route-instructies

## Omgeving
- DEVASC VM
- Python 3
- Externe API: Graphhopper Directions API
- Editor: VS Code

## Bestanden
- `graphhopper_parse-json_1.py` → eerste geocoding test
- `graphhopper_parse-json_2.py` → status & URL output
- `graphhopper_parse-json_3.py` → geocoding functie
- `graphhopper_parse-json_4.py` → tweede locatie
- `graphhopper_parse-json_5.py` → routing API
- `graphhopper_parse-json_6.py` → route parsing
- `graphhopper_parse-json_7.py` → volledige interactieve applicatie

## API Key
De Graphhopper API key wordt **niet hardcoded**.
De key wordt ingesteld via environment variable:

```bash
export GRAPHOPPER_KEY="YOUR_API_KEY"
```

## Uitvoering

Start de volledige applicatie:

export GRAPHOPPER_KEY="b6b52de4-6cc4-4dde-972b-46b22bbe561e"
python3 graphhopper_parse-json_7.py

Voorbeeld input:

Vehicle: car

Start: Washington, D.C.

Destination: Baltimore, Maryland

## Resultaat

Succesvolle Geocoding API calls (status 200)

Succesvolle Routing API call (status 200)

Afstand en reistijd berekend

Turn-by-turn route instructies weergegeven

## Bewijs

Volledige terminal run met input en output:

screenshots/ap2_01_full_run.png