# Guide de Lancement et Test des Exercices

## 📦 Installation Préalable

```bash
# Installer toutes les dépendances Python
pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended

# Vérifier les installations
python3 -c "import requests; print('requests OK')"
python3 -c "from flask import Flask; print('Flask OK')"
python3 -c "from flask_httpauth import HTTPBasicAuth; print('Flask-HTTPAuth OK')"
python3 -c "from flask_jwt_extended import JWTManager; print('Flask-JWT-Extended OK')"

# Vérifier cURL
curl --version
```

## 🎯 Par Tâche

### Task 0: HTTP/HTTPS Basics ✅

**Fichiers**: `task_00_http_https.md`

**Action**: Lire la documentation
```bash
# Ouvrir et lire
cat task_00_http_https.md
# ou avec VS Code
code task_00_http_https.md
```

**Concepts à comprendre**:
- Différences HTTP vs HTTPS
- Méthodes HTTP (GET, POST, PUT, DELETE, etc.)
- Codes de statut (200, 201, 400, 404, 500, etc.)
- Structure requête/réponse HTTP

---

### Task 1: cURL API Consumption ✅

**Fichiers**: `task_01_curl_guide.md`

**Action**: Lire le guide et tester des commandes

```bash
# Lire le guide
cat task_01_curl_guide.md

# Test simple - GET
curl https://jsonplaceholder.typicode.com/posts

# Test - GET spécifique
curl https://jsonplaceholder.typicode.com/posts/1

# Test - POST
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","body":"Content","userId":1}' \
  https://jsonplaceholder.typicode.com/posts

# Test - voir uniquement headers
curl -I https://jsonplaceholder.typicode.com/posts

# Test - pretty print JSON (si jq installé)
curl https://jsonplaceholder.typicode.com/posts/1 | python3 -m json.tool
```

**Résultat attendu**: Vous devez voir les données JSON de JSONPlaceholder

---

### Task 2: Python Requests ✅

**Fichiers**: 
- `task_02_requests.py` - Code principal
- `main_02_requests.py` - Script de démarrage
- `posts.csv` - Fichier généré

**Commande**:
```bash
# Lancer le script
python3 main_02_requests.py
```

**Sortie attendue**:
```
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
...
Successfully saved 100 posts to posts.csv
```

**Fichier généré**: `posts.csv` (avec colonnes id, title, body)

---

### Task 3: HTTP Server ✅

**Fichiers**: `task_03_http_server.py`

**Terminal 1 - Démarrer le serveur**:
```bash
python3 task_03_http_server.py
```

**Sortie attendue**:
```
Server running at http://127.0.0.1:8000
Press Ctrl+C to stop the server

Available endpoints:
  GET http://127.0.0.1:8000/          - Simple text response
  GET http://127.0.0.1:8000/data      - JSON data
  GET http://127.0.0.1:8000/status    - Status check
  GET http://127.0.0.1:8000/info      - API information
```

**Terminal 2 - Tester les endpoints**:
```bash
# Test root
curl http://localhost:8000/
# Sortie: Hello, this is a simple API!

# Test /data
curl http://localhost:8000/data
# Sortie: {"name": "John", "age": 30, "city": "New York"}

# Test /status
curl http://localhost:8000/status
# Sortie: OK

# Test /info
curl http://localhost:8000/info
# Sortie: {"version": "1.0", "description": "A simple API built with http.server"}

# Test endpoint inexistant
curl http://localhost:8000/unknown
# Sortie: {"error": "Endpoint not found"}
```

**Arrêter le serveur**: `Ctrl+C` dans Terminal 1

---

### Task 4: Flask API ✅

**Fichiers**:
- `task_04_flask.py` - API Flask
- `test_flask.py` - Script de test

**Terminal 1 - Démarrer l'API**:
```bash
python3 task_04_flask.py
```

**Sortie attendue**:
```
 * Serving Flask app 'task_04_flask.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

**Terminal 2 - Tests manuels**:
```bash
# Test home
curl http://localhost:5000/
# Sortie: Welcome to the Flask API!

# Test status
curl http://localhost:5000/status
# Sortie: OK

# Test data (empty initially)
curl http://localhost:5000/data
# Sortie: []

# Ajouter un utilisateur
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"jane","name":"Jane","age":28,"city":"Los Angeles"}' \
  http://localhost:5000/add_user

# Sortie: {"message": "User added", "user": {...}}

# Récupérer l'utilisateur
curl http://localhost:5000/users/jane

# Sortie: {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}

# Vérifier la liste
curl http://localhost:5000/data
# Sortie: ["jane"]

# Erreur - username manquant
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Test"}' \
  http://localhost:5000/add_user
# Sortie: {"error": "Username is required"} (400)

# Erreur - username dupliqué
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"jane","name":"Jane2"}' \
  http://localhost:5000/add_user
# Sortie: {"error": "Username already exists"} (409)
```

**OU lancer le script de test complet**:
```bash
# Terminal 2 (avec l'API en cours)
python3 test_flask.py
```

**Sortie attendue**:
```
==================================================
Flask API Test Suite
==================================================

Testing GET /
Status: 200
Response: Welcome to the Flask API!

Testing GET /status
Status: 200
Response: OK

...
[Suite de tests avec tous les endpoints]

==================================================
All tests completed!
==================================================
```

**Arrêter l'API**: `Ctrl+C` dans Terminal 1

---

### Task 5: Security & Authentication ✅

**Fichiers**:
- `task_05_basic_security.py` - API avec authentification
- `test_security.py` - Script de test

**Terminal 1 - Démarrer l'API sécurisée**:
```bash
python3 task_05_basic_security.py
```

**Sortie attendue**:
```
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

**Terminal 2 - Tests Basic Auth**:
```bash
# SANS authentification (doit échouer)
curl http://localhost:5000/basic-protected
# Sortie: {"error":"Unauthorized"} (401)

# AVEC authentification correcte
curl -u user1:password http://localhost:5000/basic-protected
# Sortie: Basic Auth: Access Granted

# AVEC mauvais password
curl -u user1:wrongpassword http://localhost:5000/basic-protected
# Sortie: {"error":"Unauthorized"} (401)
```

**Terminal 2 - Tests JWT**:
```bash
# 1. OBTENIR UN TOKEN

# Login utilisateur normal
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"password"}' \
  http://localhost:5000/login

# Sortie: {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}

# Copier le token
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# 2. UTILISER LE TOKEN

# SANS token
curl http://localhost:5000/jwt-protected
# Sortie: {"error": "Missing or invalid token"} (401)

# AVEC token invalide
curl -H "Authorization: Bearer invalid_token" \
  http://localhost:5000/jwt-protected
# Sortie: {"error": "Invalid token"} (401)

# AVEC token valide
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5000/jwt-protected
# Sortie: JWT Auth: Access Granted

# 3. ADMIN ONLY ENDPOINT

# Login admin
ADMIN_TOKEN=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"admin1","password":"password"}' \
  http://localhost:5000/login | jq -r '.access_token')

# Utilisateur normal essaie d'accéder
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5000/admin-only
# Sortie: {"error": "Admin access required"} (403)

# Admin accède avec succès
curl -H "Authorization: Bearer $ADMIN_TOKEN" \
  http://localhost:5000/admin-only
# Sortie: Admin Access: Granted
```

**OU lancer le script de test complet**:
```bash
# Terminal 2 (avec l'API en cours)
python3 test_security.py
```

**Sortie attendue**:
```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║     Security API Test Suite - Flask-HTTPAuth & JWT     ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

============================================================
API HOME ENDPOINT
============================================================

{
  "message": "Welcome to Secure API",
  "version": "1.0",
  ...
}

============================================================
TESTING BASIC AUTHENTICATION
============================================================

[Tests de Basic Auth]

============================================================
TESTING JWT LOGIN
============================================================

[Tests de JWT Login]

...
```

**Arrêter l'API**: `Ctrl+C` dans Terminal 1

---

## 🔄 Workflow Rapide

Pour tester TOUS les exercices rapidement:

```bash
# 1. Task 0 - Lire
cat task_00_http_https.md

# 2. Task 1 - Tester
curl https://jsonplaceholder.typicode.com/posts/1

# 3. Task 2 - Exécuter
python3 main_02_requests.py

# 4. Task 3 - Lancer serveur (Terminal A)
python3 task_03_http_server.py &
# Test (Terminal B)
curl http://localhost:8000/data

# 5. Task 4 - Lancer API (Terminal A)
python3 task_04_flask.py &
# Test (Terminal B)
python3 test_flask.py

# 6. Task 5 - Lancer API sécurisée (Terminal A)
python3 task_05_basic_security.py &
# Test (Terminal B)
python3 test_security.py
```

---

## 📊 Vérification Finale

```bash
# Vérifier que tous les fichiers existent
ls -la

# Vérifier les imports sont OK
python3 -c "import requests, flask, flask_httpauth, flask_jwt_extended; print('✅ All imports OK')"

# Tester une requête simple
python3 -c "import requests; r = requests.get('https://jsonplaceholder.typicode.com/posts/1'); print(f'✅ API call OK: {r.status_code}')"
```

---

## 🆘 Troubleshooting

### Port déjà utilisé
```bash
# Erreur: "Address already in use"

# Trouver le processus
lsof -i :5000

# Tuer le processus
kill -9 <PID>
```

### Module introuvable
```bash
# Erreur: ModuleNotFoundError

# Réinstaller
pip install --upgrade requests Flask Flask-HTTPAuth Flask-JWT-Extended
```

### Connection refused
```bash
# Erreur: "Connection refused"

# S'assurer que le serveur est démarré dans un autre terminal
python3 task_04_flask.py
```

### Mauvais authentiques (Task 5)
```bash
# Rappel:
# Username: user1, Password: password (role: user)
# Username: admin1, Password: password (role: admin)
```

---

## ✅ Checklist

- [ ] Task 0: Lu la documentation HTTP/HTTPS
- [ ] Task 1: Testé cURL avec JSONPlaceholder
- [ ] Task 2: Exécuté et créé posts.csv
- [ ] Task 3: Lancé le serveur et testé les endpoints
- [ ] Task 4: Lancé l'API Flask et exécuté les tests
- [ ] Task 5: Testé Basic Auth et JWT

---

**Créé**: 19 février 2026
**Dernière mise à jour**: 19 février 2026
