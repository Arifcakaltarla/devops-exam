# Di3 – Custom Docker Image Experiment 2 (SQL)

## Doel
Een eigen Docker image bouwen met een SQL-database (PostgreSQL) die bij de eerste start automatisch
een tabel + voorbeelddata aanmaakt, en dit verifiëren met SQL queries.

## Bestanden
- `Dockerfile` : custom image op basis van `postgres:16-alpine`
- `init.sql` : init script (tabel + inserts) via `/docker-entrypoint-initdb.d/`
- `run.sh` : build + run + test query
- `screenshots/` : bewijs

## Build & Run

### Image bouwen
```bash
docker build -t di3-postgres-demo .
```

## Container starten
docker rm -f di3-postgres 2>/dev/null || true
docker run -d --name di3-postgres \
  -e POSTGRES_DB=schooldb \
  -e POSTGRES_USER=devasc \
  -e POSTGRES_PASSWORD=devops123 \
  -p 5432:5432 \
  di3-postgres-demo

## (Sneller) via script
chmod +x run.sh
./run.sh

## Verificatie
docker ps | grep di3
docker exec -i di3-postgres psql -U devasc -d schooldb -c "\dt"
docker exec -i di3-postgres psql -U devasc -d schooldb -c "SELECT * FROM students;"

## Resultaat

Image: di3-postgres-demo

Container: di3-postgres

DB: schooldb

Tabel: students met voorbeeldrecords

## Bewijs

Zie screenshots/:

di3_docker_ps_ok.png

di3_psql_select_ok.png