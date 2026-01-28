#!/bin/bash
set -e

APP_DIR="app-tmp"
IMAGE_NAME="di1-sample-app"
CONTAINER_NAME="di1-sample-container"

rm -rf "$APP_DIR"
mkdir -p "$APP_DIR"

cp sample_app.py "$APP_DIR/"
cp -r templates static "$APP_DIR/"

cat > "$APP_DIR/Dockerfile" << 'EOF'
FROM python:3.11-slim

WORKDIR /app
COPY . /app

ENV PIP_PROGRESS_BAR=off
RUN pip install --no-cache-dir --progress-bar off flask

EXPOSE 8080
CMD ["python", "sample_app.py"]
EOF

docker build -t "$IMAGE_NAME" "$APP_DIR"

docker rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true
docker run -d --name "$CONTAINER_NAME" -p 8080:8080 "$IMAGE_NAME"

echo "Container running."
echo "Test: curl http://localhost:8080"
