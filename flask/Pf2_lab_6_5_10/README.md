# Pf2 – Logon-page / Password Methods (Lab 6.5.10)

## Doel
Aantonen waarom plaintext passwords onveilig zijn en hoe hashing (SHA256) beter is.

## Bestanden
- `password-evolution.py` – Flask API met v1 (plaintext) en v2 (hash)
- `test.db` – SQLite database met users
- `screenshots/` – bewijs (DB Browser)

## Uitvoering

### Start server
```bash
python3 password-evolution.py
```

## v1 – Plaintext signup/login
curl -k -X POST -F 'username=bob'   -F 'password=bobpw'   https://0.0.0.0:5000/signup/v1
curl -k -X POST -F 'username=alice' -F 'password=alicepw' https://0.0.0.0:5000/signup/v1

curl -k -X POST -F 'username=bob'   -F 'password=bobpw'   https://0.0.0.0:5000/login/v1
curl -k -X POST -F 'username=alice' -F 'password=wrong'   https://0.0.0.0:5000/login/v1

## v2 – Hashed signup/login (SHA256)
curl -k -X POST -F 'username=rick'  -F 'password=samepassword'      https://0.0.0.0:5000/signup/v2
curl -k -X POST -F 'username=allan' -F 'password=samepassword'      https://0.0.0.0:5000/signup/v2
curl -k -X POST -F 'username=dave'  -F 'password=differentpassword' https://0.0.0.0:5000/signup/v2

curl -k -X POST -F 'username=rick'  -F 'password=samepassword'  https://0.0.0.0:5000/login/v2
curl -k -X POST -F 'username=allan' -F 'password=wrongpassword' https://0.0.0.0:5000/login/v2
curl -k -X POST -F 'username=allan' -F 'password=samepassword'  https://0.0.0.0:5000/login/v2
curl -k -X POST -F 'username=dave'  -F 'password=differentpassword' https://0.0.0.0:5000/login/v2

## Resultaat

USER_PLAIN bevat passwords in plaintext (onveilig).

USER_HASH bevat SHA256 hashes i.p.v. plaintext.

Users met hetzelfde password krijgen dezelfde hash (geen salt).

## Bewijs

screenshots/01_user_plain.png – plaintext passwords in USER_PLAIN

screenshots/02_user_hash.png – hashes in USER_HASH