# Pv1 – Python Virtual Environment (venv)

## Doel
Een Python virtual environment aanmaken en gebruiken om packages
geïsoleerd te installeren.

## Context
Dit lab-experiment is uitgevoerd in de Cisco DEVASC VM en toont het
basisgebruik van Python venv zoals behandeld in de cursus.

## Stappen
```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
pip list
deactivate
```
## Resultaat

Virtual environment succesvol aangemaakt

Packages geïnstalleerd binnen de venv

Python en pip draaien vanuit de venv

## Bewijs

In de map screenshots/ is een afbeelding toegevoegd als visueel bewijs
van de actieve virtual environment.

## Besluit

Dit experiment toont hoe Python venv gebruikt wordt om afhankelijkheden
geïsoleerd en gecontroleerd te beheren.