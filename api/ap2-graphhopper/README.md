# Ap2 – Integrate a REST API in a Python Application (GraphHopper)

## Doel
Dit experiment implementeert stap voor stap een Python applicatie die:
- JSON data ophaalt via de GraphHopper REST API
- Geocoding en routing uitvoert
- Resultaten verwerkt en toont aan de gebruiker

Het experiment volgt **exact Lab 4.9.2** uit Cisco NetAcad.

---

## Overzicht van de scripts (volgens het lab)

### graphhopper_parse-json_1.py
- Eerste test van de GraphHopper Geocoding API
- Ophalen en afdrukken van de volledige JSON-response

### graphhopper_parse-json_2.py
- Controleren van de HTTP statuscode
- Afdrukken van de gebruikte Geocoding API URL

### graphhopper_parse-json_3.py
- Opdelen van de code in functies
- Geocoding van start- en bestemmingslocatie

### graphhopper_parse-json_4.py
- Uitgebreide geocoding functie
- Teruggeven van statuscode, latitude en longitude

### graphhopper_parse-json_5.py
- Toevoegen van routing functionaliteit
- Berekenen van:
  - afstand (km)
  - reistijd (minuten)

### graphhopper_parse-json_6.py
- Formatteren van output:
  - afstand in km en miles
  - reistijd in hh:mm:ss
- Tonen van turn-by-turn instructies

### graphhopper_parse-json_7.py (FINAL)
- Volledige interactieve applicatie
- Gebruiker voert zelf in:
  - voertuigtype (car, bike, foot)
  - startlocatie
  - bestemming
- Volledige route-informatie wordt weergegeven

---

## API Key (veilig gebruik)
De GraphHopper API key wordt **niet hardcoded** en **niet gepusht naar GitHub**.

De key wordt lokaal ingesteld via een environment variable.

## test
python3 graphhopper_parse-json_7.py

- Washington, D.C.
- Baltimore, Maryland

- Brussels, Belgium
- Antwerp, Belgium

