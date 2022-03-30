# Event-driven System

This is a simple event-driven system that is used to add current time to a chat message. It could be used to scale to larger projects.

## Requirements:
- Python 3.10
- GCP account with Pub/Sub services

## Quickstart (Unix/MacOS):
### 1. Prepare .env file with Pub/Sub credentials
```
touch .env
echo 'GOOGLE_APPLICATION_CREDENTIALS="<PATH_TO_JSON_KEY>"' >> .env
echo 'PROJECT_ID="<PROJECT_ID>"' >> .env
echo 'TOPIC_ID="<TOPIC_ID>"' >> .env
```
### 2. Install Python deps
```
python3 -m venv .venv
source .venv/bin/activate
pip install -m requirements.txt
```
### 3. Run the code
```
source .venv/bin/activate
python src/main.py
```