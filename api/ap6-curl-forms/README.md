# AP6 – REST API experiment with curl (forms)

## Description
Flask REST API that accepts form data.
Tested using curl with application/x-www-form-urlencoded.

## Run
```bash
pip3 install flask
python3 app_forms.py
API runs on:

http://localhost:5002

curl form tests
See curl_forms_commands.txt.

Examples:
curl -i -X POST http://localhost:5002/api/login -d "username=student" -d "password=devops"
curl -i -X POST http://localhost:5002/api/feedback -d "name=Arif" -d "message=AP6 curl forms works"
