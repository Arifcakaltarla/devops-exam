#!/bin/bash
set -e

IMAGE="di3-postgres-demo"
NAME="di3-postgres"
DB="schooldb"
USER="devasc"
PASS="devops123"

docker build -t "$IMAGE" .

docker rm -f "$NAME" >/dev/null 2>&1 || true

docker run -d --name "$NAME" \
  -e POSTGRES_DB="$DB" \
  -e POSTGRES_USER="$USER" \
  -e POSTGRES_PASSWORD="$PASS" \
  -p 5432:5432 \
  "$IMAGE"

echo "Waiting for Postgres..."
sleep 3

echo "Test query:"
docker exec -i "$NAME" psql -U "$USER" -d "$DB" -c "SELECT * FROM students;"
