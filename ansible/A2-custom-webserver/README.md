# A2 – Ansible: Custom Webserver Experiment

## Doel
Een eigen Ansible playbook ontwikkelen om een webserver automatisch
te installeren en een custom webpagina te deployen.

## Context
Dit experiment bouwt verder op A1 en toont een eigen toepassing van
Infrastructure as Code (IaC) met Ansible in de Cisco DEVASC VM.

## Gebruikte technologieën
- Ansible
- Apache2
- Ubuntu (DEVASC VM)

## Bestanden
- `ansible.cfg` – Ansible configuratie
- `hosts` – inventory met webservers
- `install_custom_webpage.yaml` – playbook voor Apache + custom webpagina
- `screenshots/` – visueel bewijs

## Uitvoering
```bash
ansible-playbook install_custom_webpage.yaml
```
## Resultaat
- Apache2 automatisch geïnstalleerd
- Custom `index.html` gedeployed via Ansible
- Webserver bereikbaar via `http://192.0.2.3:8081`

## Bewijs
In de map `screenshots/` is een afbeelding toegevoegd als visueel bewijs
van de werkende custom webpagina.

## Besluit
Dit experiment toont hoe Ansible gebruikt kan worden om zowel
infrastructuur als applicatie-content automatisch te deployen.
