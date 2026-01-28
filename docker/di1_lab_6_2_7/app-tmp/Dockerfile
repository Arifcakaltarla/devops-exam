FROM python:3.11-slim

WORKDIR /app
COPY . /app

ENV PIP_PROGRESS_BAR=off
RUN pip install --no-cache-dir --progress-bar off flask

EXPOSE 8080
CMD ["python", "sample_app.py"]
