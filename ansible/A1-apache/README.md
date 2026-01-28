# A1 – Ansible: Automate Installing a Web Server (Apache)

## Doel
Automatisch installeren en configureren van een Apache webserver met Ansible.

## Context
Dit experiment werd uitgevoerd in de Cisco DEVASC VM en is gebaseerd op het
NetAcad lab **“Use Ansible to Automate Installing a Web Server”**.

## Gebruikte technologieën
- Ansible
- Apache2
- Ubuntu (DEVASC VM)

## Bestanden
- `hosts` – Ansible inventory met webservers
- `ansible.cfg` – lokale Ansible configuratie
- `test_apache_playbook.yaml` – test communicatie met webserver
- `install_apache_playbook.yaml` – installeert Apache + mod_rewrite
- `install_apache_options_playbook.yaml` – configureert Apache op poort 8081
- `screenshots/` – visueel bewijs van uitvoering

## Uitvoering
```bash
ansible webservers -m ping
ansible-playbook test_apache_playbook.yaml
ansible-playbook install_apache_playbook.yaml
ansible-playbook install_apache_options_playbook.yaml

##Resultaat

Apache2 succesvol geïnstalleerd

mod_rewrite geactiveerd

Webserver luistert op poort 8081

Apache bereikbaar via browser: http://192.0.2.3:8081

Besluit

Dit experiment toont hoe Ansible gebruikt kan worden om webservers
geautomatiseerd, schaalbaar en reproduceerbaar te configureren.

## Bewijs
In de map `screenshots/` zijn afbeeldingen toegevoegd als visueel bewijs van:
- Werkende Apache webserver op poort 8081