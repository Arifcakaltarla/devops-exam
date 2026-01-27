# AP5 – API Testing with cURL

## Doel
In deze opdracht wordt een REST API getest met **cURL** via de terminal.
De focus ligt op het uitvoeren van HTTP requests zonder Python, puur via command line tools.

## Gebruikte tools
- DEVASC VM
- cURL
- Bash terminal

## Bestanden
- `curl_commands.txt` – Bevat alle uitgevoerde cURL-commando’s
- `app_api.py` – (optioneel) API-script dat getest werd met cURL

## Uitgevoerde testen
De volgende API-acties werden getest met cURL:

- GET request
- POST request
- Gebruik van headers
- Gebruik van JSON body
- Controleren van HTTP status codes
- Testen van API-responses

## Voorbeeld: cURL testen uitvoeren
```bash
curl -X GET http://localhost:5000

curl -X POST http://localhost:5000 \
-H "Content-Type: application/json" \
-d '{"key":"value"}'

De volledige lijst met testcommando’s staat in curl_commands.txt.

Resultaat

Alle cURL-requests werden succesvol uitgevoerd en de API gaf correcte responses terug.
Dit toont aan dat de API correct bereikbaar en testbaar is via cURL.

Status

✅ AP5 succesvol afgerond
