# A3 – Ansible: NGINX Webserver Experiment

## Doel
Een eigen Ansible playbook maken voor een andere service dan Apache,
namelijk NGINX.

## Context
Dit experiment toont hoe meerdere services met Ansible geautomatiseerd
kunnen worden binnen dezelfde omgeving.

## Gebruikte technologieën
- Ansible
- NGINX
- Ubuntu (DEVASC VM)

## Bestanden
- `ansible.cfg` – Ansible configuratie
- `hosts` – inventory met webservers
- `install_nginx.yaml` – playbook voor NGINX
- `screenshots/` – visueel bewijs

## Uitvoering
```bash
ansible-playbook install_nginx.yaml
```
## Resultaat

NGINX automatisch geïnstalleerd

Custom webpagina gedeployed

Webserver bereikbaar via http://192.0.2.3

## Bewijs

In de map screenshots/ is een afbeelding toegevoegd als visueel bewijs
van de werkende NGINX webserver.

## Besluit

Dit experiment toont hoe Ansible flexibel ingezet kan worden voor het
automatiseren van verschillende services.