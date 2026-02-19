# Guide Complet des APIs RESTful - De A à Z

## Table des Matières
1. [Introduction aux APIs](#introduction)
2. [Task 0: HTTP/HTTPS Basics](#task-0)
3. [Task 1: cURL - Consommer une API](#task-1)
4. [Task 2: Python Requests - Traiter les données](#task-2)
5. [Task 3: http.server - Créer une API simple](#task-3)
6. [Task 4: Flask - API complète](#task-4)
7. [Task 5: Sécurité et Authentification](#task-5)

---

## Introduction aux APIs {#introduction}

### Qu'est-ce qu'une API REST?

Une **API RESTful** (Representational State Transfer) est une interface qui permet aux applications de:
- **Demander** des données (GET)
- **Créer** des ressources (POST)
- **Modifier** des ressources (PUT/PATCH)
- **Supprimer** des ressources (DELETE)

### Architecture Client-Serveur

```
┌────────┐         ┌─────────────┐         ┌───────────┐         ┌──────────┐
│ Client │ Request │ Web Server  │ Process │ API Logic │ Fetch   │ Database │
│        ├────────►│             ├────────►│           ├────────►│          │
│        │         │             │         │           │         │          │
│        │ Response│ ◄───────────│ Return  │ ◄────────│ Result  │          │
└────────┘         └─────────────┘         └───────────┘         └──────────┘
```

### Avantages des APIs RESTful

✅ **Scalabilité**: Chaque requête est indépendante (stateless)
✅ **Flexibilité**: Fonctionne avec n'importe quel client
✅ **Cacheable**: Les réponses peuvent être cachées
✅ **Uniformité**: Standard HTTP bien établi
✅ **Décuplage**: Client et serveur indépendants

---

## Task 0: HTTP/HTTPS Basics {#task-0}

### HTTP vs HTTPS

| Aspect | HTTP | HTTPS |
|--------|------|-------|
| **Encryption** | ❌ Aucune | ✅ SSL/TLS |
| **Port** | 80 | 443 |
| **Sécurité** | Vulnérable | Protégée |
| **Certificat** | Non requis | Requis |
| **Cas d'usage** | Public | Sensible |

### Structure de la Requête HTTP

```http
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer token123
Content-Length: 42

{"username": "john", "email": "john@example.com"}
```

**Composants:**
- **Ligne de requête**: Méthode, chemin, version HTTP
- **Headers**: Métadonnées (type de contenu, authentification, etc.)
- **Corps (Body)**: Données à envoyer

### Structure de la Réponse HTTP

```http
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 89
Set-Cookie: sessionId=abc123; Path=/

{"id": 5, "username": "john", "email": "john@example.com", "created_at": "2024-01-15"}
```

**Composants:**
- **Ligne de statut**: Version, code, message
- **Headers**: Métadonnées de réponse
- **Corps**: Réponse avec données

### Méthodes HTTP Courantes

```python
GET    /posts           # Récupérer tous les posts
GET    /posts/1         # Récupérer le post numéro 1
POST   /posts           # Créer un nouveau post
PUT    /posts/1         # Remplacer le post numéro 1 complètement
PATCH  /posts/1         # Modifier partiellement le post numéro 1
DELETE /posts/1         # Supprimer le post numéro 1
```

### Codes HTTP Principaux

```
2xx - Succès
  200 OK              ✅ Requête réussie
  201 Created         ✅ Ressource créée
  204 No Content      ✅ Succès, pas de contenu

3xx - Redirection
  301 Moved           → Redirection permanente
  302 Found           → Redirection temporaire
  304 Not Modified    ↻ Utiliser le cache

4xx - Erreur Client
  400 Bad Request     ❌ Requête invalide
  401 Unauthorized    🔒 Authentification requise
  403 Forbidden       🚫 Accès refusé
  404 Not Found       ❓ Ressource inexistante
  409 Conflict        ⚠️  Conflit (doublon)

5xx - Erreur Serveur
  500 Internal Error  💥 Erreur serveur
  503 Unavailable     🔧 Service en maintenance
```

---

## Task 1: cURL - Consommer une API {#task-1}

### Introduction à cURL

**cURL** est un outil ligne de commande pour faire des requêtes HTTP.

### Installation

```bash
# Linux/Mac (généralement pré-installé)
curl --version

# Windows (via WSL ou PowerShell)
# PowerShell a généralement curl en alias
curl --version
```

### Syntaxe Basique

```bash
curl [OPTIONS] [URL]
```

### Exemples Pratiques

#### 1. Récupérer des données (GET)

```bash
# Simple GET
curl https://jsonplaceholder.typicode.com/posts

# Voir les headers aussi
curl -i https://jsonplaceholder.typicode.com/posts

# Voir SEULEMENT les headers
curl -I https://jsonplaceholder.typicode.com/posts
```

#### 2. Créer une ressource (POST)

```bash
# POST avec données de formulaire
curl -X POST \
  -d "title=Test&body=Content&userId=1" \
  https://jsonplaceholder.typicode.com/posts

# POST avec JSON
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","body":"Content","userId":1}' \
  https://jsonplaceholder.typicode.com/posts
```

#### 3. Mettre à jour une ressource (PUT)

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"id":1,"title":"Updated","body":"New body","userId":1}' \
  https://jsonplaceholder.typicode.com/posts/1
```

#### 4. Supprimer une ressource (DELETE)

```bash
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

#### 5. Authentification

```bash
# Basic Auth
curl -u username:password https://api.example.com/protected

# Bearer Token
curl -H "Authorization: Bearer your_token_here" \
  https://api.example.com/protected
```

#### 6. Pretty Print JSON

```bash
# Avec jq (si installé)
curl https://jsonplaceholder.typicode.com/posts/1 | jq .

# Avec Python
curl https://jsonplaceholder.typicode.com/posts/1 | python3 -m json.tool
```

### Flags Utiles

| Flag | Usage | Exemple |
|------|-------|---------|
| `-X METHOD` | Spécifier la méthode | `curl -X POST` |
| `-H` | Ajouter header | `curl -H "Content-Type: application/json"` |
| `-d` | Envoyer données | `curl -d "key=value"` |
| `-i` | Headers + body | `curl -i https://...` |
| `-I` | Headers seulement | `curl -I https://...` |
| `-u` | Authentication | `curl -u user:pass https://...` |
| `-L` | Suivre redirects | `curl -L https://...` |
| `-o` | Sauvegarder fichier | `curl -o file.txt https://...` |
| `-w` | Format custom | `curl -w "%{http_code}"` |

### JSONPlaceholder - API de Test

JSONPlaceholder est une API gratuite pour tester:

```bash
# Récupérer tous les posts
curl https://jsonplaceholder.typicode.com/posts

# Récupérer un post spécifique
curl https://jsonplaceholder.typicode.com/posts/1

# Récupérer les commentaires
curl https://jsonplaceholder.typicode.com/comments

# Récupérer les utilisateurs
curl https://jsonplaceholder.typicode.com/users

# Filtrer (si l'API le supporte)
curl "https://jsonplaceholder.typicode.com/posts?userId=1"
```

---

## Task 2: Python Requests - Traiter les Données {#task-2}

### Introduction à Requests

`requests` est la librairie Python standard pour HTTP.

### Installation

```bash
pip install requests
```

### Structure du Code

```python
import requests
import csv

# 1. FAIRE UNE REQUÊTE
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# 2. VÉRIFIER LE STATUT
print(f"Status Code: {response.status_code}")

# 3. PARSER LE JSON
data = response.json()

# 4. TRAITER LES DONNÉES
for post in data:
    print(post["title"])

# 5. SAUVEGARDER EN CSV
```

### Fonctions Principales de Requests

#### Requêtes HTTP

```python
import requests

# GET
response = requests.get(url)

# POST
response = requests.post(url, json={"key": "value"})

# PUT
response = requests.put(url, json={"key": "value"})

# PATCH
response = requests.patch(url, json={"key": "value"})

# DELETE
response = requests.delete(url)
```

#### Accéder aux Réponses

```python
response = requests.get(url)

# Status Code
response.status_code  # 200, 404, 500, etc.

# Headers
response.headers  # Dict de headers

# Contenu brut
response.text  # Chaîne
response.content  # Bytes

# JSON parsé
response.json()  # Dict ou List

# Encoding
response.encoding  # "utf-8"

# URL finale (après redirects)
response.url

# Historique (redirects)
response.history
```

#### Requêtes avec Options

```python
# Headers
headers = {"User-Agent": "MyApp/1.0"}
response = requests.get(url, headers=headers)

# Paramètres de requête
params = {"userId": 1, "limit": 10}
response = requests.get(url, params=params)
# Équivaut à: https://api.example.com/posts?userId=1&limit=10

# Authentification Basic
response = requests.get(url, auth=("user", "pass"))

# JSON automatiquement encodé
response = requests.post(url, json={"key": "value"})

# Timeout
response = requests.get(url, timeout=5)

# Certificat SSL (pour HTTPS)
response = requests.get(url, verify=True)  # Vérifier certificat
response = requests.get(url, verify=False)  # Ignorer certificat

# Redirection
response = requests.get(url, allow_redirects=True)
```

### Traitement des Données JSON

```python
import requests
import csv

def fetch_and_process():
    # Récupérer les données
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if response.status_code == 200:
        posts = response.json()
        
        # Extraire les champs souhaités
        posts_simple = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]
        
        # Sauvegarder en CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_simple)

fetch_and_process()
```

### Gestion des Erreurs

```python
import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()  # Lève exception si status >= 400
    
    data = response.json()
    
except requests.exceptions.ConnectionError:
    print("Erreur de connexion")
except requests.exceptions.Timeout:
    print("Timeout")
except requests.exceptions.HTTPError as e:
    print(f"Erreur HTTP: {e}")
except requests.exceptions.RequestException as e:
    print(f"Erreur: {e}")
```

---

## Task 3: http.server - Créer une API Simple {#task-3}

### Introduction à http.server

`http.server` est le module Python standard pour créer un serveur HTTP basique.

**Avantages:**
- Pas de dépendance externe
- Idéal pour apprendre
- Utile pour prototyper rapidement

**Limitations:**
- Pas de features avancées
- Pas de production (une seule requête à la fois)
- Pas de routing automatique

### Structure d'un Serveur HTTP

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Gérer les requêtes GET
        print(f"Chemin: {self.path}")
        print(f"Headers: {self.headers}")
        
        # Envoyer réponse
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello World")
    
    def do_POST(self):
        # Gérer les requêtes POST
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        
        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"message": "Created"}')

# Démarrer le serveur
if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), MyHandler)
    print("Serveur sur http://127.0.0.1:8000")
    server.serve_forever()
```

### Métodes Principales

#### Envoyer une Réponse

```python
# 1. Envoyer le code de statut
self.send_response(200)  # OK
self.send_response(201)  # Created
self.send_response(404)  # Not Found
self.send_response(500)  # Internal Server Error

# 2. Envoyer les headers
self.send_header("Content-type", "application/json")
self.send_header("Cache-Control", "no-cache")

# 3. Terminer les headers
self.end_headers()

# 4. Envoyer le corps
self.wfile.write(b"Response body here")
self.wfile.write(json.dumps(data).encode("utf-8"))
```

#### Récupérer les Paramètres

```python
def do_GET(self):
    # URL et chemin
    print(self.path)  # "/data?id=1"
    
    # Parsing du chemin
    from urllib.parse import urlparse, parse_qs
    parsed = urlparse(self.path)
    path = parsed.path  # "/data"
    params = parse_qs(parsed.query)  # {"id": ["1"]}
    
    # Headers
    self.headers["Content-Type"]
    self.headers["Authorization"]
```

#### Lire les Données POST

```python
def do_POST(self):
    # Récupérer la longueur du contenu
    content_length = int(self.headers.get("Content-Length", 0))
    
    # Lire le corps
    body = self.rfile.read(content_length)
    
    # Parser JSON
    import json
    data = json.loads(body.decode("utf-8"))
```

### Routing Simple

```python
def do_GET(self):
    if self.path == "/":
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Home")
    
    elif self.path == "/data":
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"key": "value"}).encode())
    
    else:
        self.send_response(404)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "Not found"}).encode())
```

### Exemple Complet

Voir `task_03_http_server.py` pour l'implémentation complète avec:
- Endpoint "/" (texte simple)
- Endpoint "/data" (JSON)
- Endpoint "/status" (vérification de statut)
- Endpoint "/info" (informations API)
- Gestion des 404

---

## Task 4: Flask - API Complète {#task-4}

### Introduction à Flask

Flask est un micro-framework léger pour créer des applications web et APIs.

**Avantages:**
- Syntaxe simple et intuitive
- Extensible avec plugins
- Production-ready
- Grande communauté

### Installation

```bash
pip install Flask
```

### Structure Basique

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue!"

@app.route("/api/data")
def get_data():
    return jsonify({"key": "value"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

### Définir les Routes

#### Routes Simples

```python
# GET simple
@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify([{"id": 1, "title": "Post 1"}])

# POST
@app.route("/posts", methods=["POST"])
def create_post():
    return jsonify({"message": "Created"}), 201

# Plusieurs méthodes
@app.route("/posts/<id>", methods=["GET", "PUT", "DELETE"])
def handle_post(id):
    if request.method == "GET":
        return jsonify({"id": id})
    elif request.method == "PUT":
        return jsonify({"message": "Updated"})
    else:
        return jsonify({"message": "Deleted"})
```

#### Paramètres Dynamiques

```python
# Paramètre dans l'URL
@app.route("/users/<username>")
def get_user(username):
    return jsonify({"username": username})

# Avec type
@app.route("/posts/<int:post_id>")
def get_post(post_id):
    return jsonify({"id": post_id, "type": type(post_id)})
```

#### Paramètres de Requête

```python
@app.route("/search")
def search():
    query = request.args.get("q", "")
    limit = request.args.get("limit", 10, type=int)
    return jsonify({"query": query, "limit": limit})

# Utilisation: /search?q=python&limit=5
```

### Recevoir des Données

#### JSON

```python
@app.route("/users", methods=["POST"])
def add_user():
    # Récupérer JSON
    data = request.get_json()
    
    username = data.get("username")
    email = data.get("email")
    
    return jsonify({
        "message": "User created",
        "username": username
    }), 201
```

#### Formulaire

```python
@app.route("/submit", methods=["POST"])
def submit_form():
    # Données de formulaire
    name = request.form.get("name")
    email = request.form.get("email")
    
    return jsonify({"message": f"Hello {name}"})
```

### Réponses

#### JSON

```python
# Dict → JSON
return jsonify({"key": "value"})

# List → JSON
return jsonify([1, 2, 3])

# Avec code de statut
return jsonify({"message": "Created"}), 201

# Avec headers
response = jsonify({"key": "value"})
response.headers["X-Custom"] = "Header"
return response
```

#### Texte

```python
return "Texte simple"
return "<h1>HTML</h1>", 200, {"Content-Type": "text/html"}
```

#### Fichiers

```python
from flask import send_file

@app.route("/download")
def download():
    return send_file("file.pdf")
```

### Gestion des Erreurs

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Server error"}), 500
```

### Stockage de Données en Mémoire

Pour l'exercice, on utilise un dictionnaire:

```python
users = {}

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    
    users[username] = data
    return jsonify(data), 201

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "Not found"}), 404
```

### Vérifications et Validations

```python
@app.route("/add_user", methods=["POST"])
def add_user():
    # Vérifier JSON
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400
    
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # Vérifier champs requis
    if "username" not in data:
        return jsonify({"error": "Username required"}), 400
    
    username = data.get("username")
    
    # Vérifier duplicatas
    if username in users:
        return jsonify({"error": "Username exists"}), 409
    
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201
```

### Démarrer le Serveur

```bash
# Mode développement
python3 task_04_flask.py

# Ou avec Flask CLI
flask --app task_04_flask.py run

# Avec options
flask --app task_04_flask.py run --host 0.0.0.0 --port 8000
```

### Test avec cURL

```bash
# GET
curl http://localhost:5000/

# GET avec paramètre
curl http://localhost:5000/users/jane

# POST
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"john","name":"John"}' \
  http://localhost:5000/add_user

# PUT
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"username":"john","age":30}' \
  http://localhost:5000/users/john

# DELETE
curl -X DELETE http://localhost:5000/users/jane
```

---

## Task 5: Sécurité et Authentification {#task-5}

### Importance de la Sécurité

Les APIs doivent protéger:
- 🔒 Les données sensibles
- 🔑 L'accès non autorisé
- 🚫 Les attaques malveillantes
- 📊 Les abus de ressources

### Authentification vs Autorisation

| Aspect | Authentification | Autorisation |
|--------|------------------|--------------|
| **But** | Vérifier l'identité | Vérifier les permissions |
| **Question** | "Qui êtes-vous?" | "Pouvez-vous faire ça?" |
| **Exemple** | Login avec mot de passe | Accès admin seulement |

### 1. Authentification Basique (Basic Auth)

#### Concept

L'utilisateur envoie `username:password` en Base64.

```
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
                      ↑ Base64(username:password)
```

#### Implémentation avec Flask-HTTPAuth

```bash
pip install Flask-HTTPAuth
```

```python
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route("/protected")
@auth.login_required
def protected():
    return f"Hello {auth.current_user()}"
```

#### Test

```bash
# Sans credentials
curl http://localhost:5000/protected
# → 401 Unauthorized

# Avec credentials
curl -u user1:password http://localhost:5000/protected
# → Success
```

#### Limitations

❌ Mot de passe envoyé à chaque requête
❌ Pas de session
❌ Acceptor HTTPS obligatoire en production

### 2. Authentification JWT (Token)

#### Concept

1. L'utilisateur se connecte → Reçoit un **token**
2. Le token est envoyé à chaque requête
3. Le serveur valide le token sans faire de requête DB

#### Structure JWT

```
Header.Payload.Signature

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9  (Header)
.
eyJzdWIiOiIxMjM0NTY3ODkwIiwiYWRtaW4iOnRydWV9  (Payload)
.
TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ  (Signature)
```

**Header**: Algorithme et type
```json
{"alg": "HS256", "typ": "JWT"}
```

**Payload**: Données (claims)
```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true,
  "iat": 1516239022
}
```

**Signature**: Hash du header + payload + secret
```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret
)
```

#### Avantages JWT

✅ Stateless (pas de session DB)
✅ Scalable (distribué facilement)
✅ Inclut les données utilisateur
✅ Signature vérifie l'intégrité

#### Implémentation avec Flask-JWT-Extended

```bash
pip install Flask-JWT-Extended
```

```python
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Endpoint de login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    # Vérifier les credentials
    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Créer le token
    token = create_access_token(identity=username)
    return jsonify({"access_token": token})

# Endpoint protégé
@app.route("/protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return f"Hello {current_user}"
```

#### Test JWT

```bash
# 1. Récupérer le token
TOKEN=$(curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"password"}' \
  http://localhost:5000/login | jq -r '.access_token')

echo $TOKEN
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# 2. Utiliser le token
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5000/protected
# → Success
```

### 3. Contrôle d'Accès Basé sur les Rôles (RBAC)

#### Concept

Attribuer des rôles aux utilisateurs et contrôler l'accès par rôle.

```python
users = {
    "user1": {"username": "user1", "password": hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": hash("password"), "role": "admin"}
}
```

#### Implémentation

```python
@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    
    if users[current_user].get("role") != "admin":
        return jsonify({"error": "Admin required"}), 403
    
    return "Admin Access Granted"
```

#### Décorateur Réutilisable

```python
from functools import wraps

def require_role(role):
    @wraps
    def decorator(fn):
        @jwt_required()
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            if users[current_user].get("role") != role:
                return jsonify({"error": f"{role} required"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@app.route("/admin-only")
@require_role("admin")
def admin_only():
    return "Admin Access"
```

### 4. Hachage des Mots de Passe

**JAMAIS** stocker les mots de passe en clair!

```bash
pip install werkzeug
```

```python
from werkzeug.security import generate_password_hash, check_password_hash

# Créer un hash
hashed = generate_password_hash("password123")
# → pbkdf2:sha256$1000$...

# Vérifier
if check_password_hash(hashed, "password123"):
    print("Correct!")
```

### 5. Gestion des Erreurs d'Authentification

```python
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

@jwt.unauthorized_loader
def handle_unauthorized(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(err):
    return jsonify({"error": "Token expired"}), 401
```

### Bonnes Pratiques de Sécurité

#### ✅ À Faire

1. **Toujours HTTPS en production**
   ```bash
   # NOT OK en production
   http://api.example.com
   
   # OK
   https://api.example.com
   ```

2. **Valider les entrées**
   ```python
   if not data.get("username"):
       return jsonify({"error": "Username required"}), 400
   ```

3. **Hacher les mots de passe**
   ```python
   hashed = generate_password_hash(password)
   ```

4. **Utiliser des secrets forts**
   ```python
   # ❌ Mauvais
   JWT_SECRET_KEY = "123456"
   
   # ✅ Bon
   JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")  # Variable env
   ```

5. **Limiter les requêtes (Rate Limiting)**
   ```bash
   pip install Flask-Limiter
   ```
   ```python
   from flask_limiter import Limiter
   limiter = Limiter(app)
   
   @app.route("/api/data")
   @limiter.limit("100 per hour")
   def get_data():
       return jsonify({})
   ```

6. **CORS (Cross-Origin Resource Sharing)**
   ```bash
   pip install Flask-CORS
   ```
   ```python
   from flask_cors import CORS
   CORS(app)
   ```

#### ❌ À Éviter

1. **Stocker les mots de passe en clair**
2. **Envoyer les mots de passe dans l'URL**
3. **Tokens sans expiration**
4. **Secrets codés en dur**
5. **HTTP en production**
6. **Pas de validation d'entrée**

### Flux Complet d'Authentification

```
1. REGISTRATION (Optionnel)
   POST /register
   Body: {username, password, ...}
   ↓
   Hash password → Store in DB
   Response: Success

2. LOGIN
   POST /login
   Body: {username, password}
   ↓
   Verify credentials → Create JWT
   Response: {access_token: "..."}

3. AUTHENTICATED REQUEST
   GET /protected
   Headers: Authorization: Bearer <token>
   ↓
   Validate token → Extract user → Execute
   Response: {data: "..."}

4. LOGOUT (Optionnel)
   POST /logout
   Headers: Authorization: Bearer <token>
   ↓
   Blacklist token
   Response: Success
```

---

## Résumé Complet

### Chemin d'Apprentissage

1. **Task 0**: Comprendre les basics HTTP/HTTPS
2. **Task 1**: Consommer une API avec cURL
3. **Task 2**: Traiter les données avec Python
4. **Task 3**: Créer un serveur basique
5. **Task 4**: Construire une API complète
6. **Task 5**: Sécuriser l'API

### Concepts Clés à Retenir

| Concept | Explication |
|---------|------------|
| **REST** | Architecture pour APIs (GET, POST, PUT, DELETE) |
| **HTTP Methods** | GET (lire), POST (créer), PUT (remplacer), PATCH (modifier), DELETE (supprimer) |
| **Status Codes** | 2xx (succès), 3xx (redirection), 4xx (erreur client), 5xx (erreur serveur) |
| **JSON** | Format standard pour l'échange de données |
| **cURL** | Outil pour tester les APIs |
| **Requests** | Librairie Python pour HTTP |
| **http.server** | Module Python pour serveur simple |
| **Flask** | Framework pour APIs plus complexes |
| **Basic Auth** | Authentication avec username:password en Base64 |
| **JWT** | Token stateless pour authentication |
| **Hachage** | Sécuriser les mots de passe |

### Files Structure

```
restful-api/
├── task_00_http_https.md      # Documentation HTTP/HTTPS
├── task_01_curl_guide.md      # Guide d'utilisation de cURL
├── task_02_requests.py        # Consommation d'API avec Python
├── main_02_requests.py        # Script de test pour Task 2
├── task_03_http_server.py     # Serveur HTTP basique
├── task_04_flask.py           # API complète avec Flask
├── test_flask.py              # Tests pour l'API Flask
├── task_05_basic_security.py  # API avec authentification
├── test_security.py           # Tests pour la sécurité
└── explanation.md             # Ce fichier!
```

### Commandes Utiles

```bash
# Installer les dépendances
pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended

# Test Task 2
python3 task_02_requests.py

# Démarrer Task 3
python3 task_03_http_server.py
# http://localhost:8000

# Démarrer Task 4
python3 task_04_flask.py
python3 test_flask.py  # Dans un autre terminal

# Démarrer Task 5
python3 task_05_basic_security.py
python3 test_security.py  # Dans un autre terminal
```

### Prochaines Étapes

Pour approfondir:
- Ajouter une vraie base de données (SQLite, PostgreSQL)
- Implémenter les migrations (Alembic)
- Ajouter de la cache (Redis)
- Documenter avec OpenAPI/Swagger
- Ajouter des tests automatisés
- Déployer en production (Heroku, AWS, etc.)

---

**Créé le**: 19 février 2026
**Auteur**: Guide d'apprentissage APIs RESTful
**Niveau**: Débutant à Intermédiaire
**Durée estimée**: 15-20 heures

Bonne couche! 🚀
