# Ap1 – School Library API (Lab 4.5.5)

## Doel
REST API’s verkennen met de School Library API Simulator:
- requests testen (GET met query params)
- authenticatie (loginViaBasic)
- boeken toevoegen via Python script

## Omgeving
- DEVASC VM
- URL: http://library.demo.local
- Tools: Postman, Python3 (requests, faker)

## Uitvoering (stappen)

### 1) GET /api/v1/books (met query params)
**In Postman:**
- Method: GET
- URL: `http://library.demo.local/api/v1/books`
- Params:
  - `includeISBN=true`
  - `sortBy=author`

### 2) (Auth) POST /api/v1/loginViaBasic
De Python script gebruikt Basic Auth om een token (X-API-Key) op te halen via:
- Endpoint: `POST http://library.demo.local/api/v1/loginViaBasic`

### 3) 100 boeken toevoegen via Python (faker)
Script uitvoeren vanuit de school-library map in de VM:

```bash
cd ~/labs/devnet-src/school-library
python3 add100RandomBooks.py
```
## Extra:
 om “hangen” te vermijden is timeout=5 toegevoegd bij de requests.post() calls (login en addBook).

## Resultaat

De API geeft een gesorteerde lijst terug via query params.

Het script voegt ~100 boeken toe (IDs 4 t.e.m. 104).

In de browser is de uitgebreide boekenlijst zichtbaar.

## Bewijs (screenshots)

Browser boekenlijst: screenshots/ap1_01_browser_books.png