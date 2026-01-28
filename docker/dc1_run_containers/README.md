# Dc1 – Run Containers Experiment

## Doel
Aantonen dat containers kunnen worden gestart, gestopt en bekeken met Docker.

## Uitvoering
```bash
docker run --name dc1-nginx -p 8082:80 nginx
# container draaien in foreground
CTRL+C

docker ps -a
```
## Resultaat

Container dc1-nginx succesvol gestart

Container correct gestopt en zichtbaar als Exited

## Bewijs

Zie screenshots/:
- dc1_docker_ps_ok.png