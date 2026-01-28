# Dm1 – Docker Management Experiment

## Doel
Aantonen dat Docker containers beheerd kunnen worden: monitoring, inspectie, pauzeren/hervatten en opruimen.

## Uitvoering
```bash
docker run -d --name dm1-nginx -p 8083:80 nginx
docker ps
docker stats --no-stream
docker inspect dm1-nginx
docker pause dm1-nginx
docker unpause dm1-nginx
docker logs dm1-nginx --tail 20
docker stop dm1-nginx
docker rm dm1-nginx
```

## Resultaat

Container gemonitord met docker stats

Status gewijzigd met pause/unpause

Logs en inspectie succesvol geraadpleegd

Container proper gestopt en verwijderd

## Bewijs

Zie screenshots/:

dm1_docker_stats_ok.png

dm1_docker_pause_ok.png