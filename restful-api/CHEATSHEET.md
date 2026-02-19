# RESTful APIs - Cheat Sheet

## 🌐 REST Principles

REST = **Representational State Transfer**

4 concepts clés:
1. **Client-Server**: Séparation claire des responsabilités
2. **Stateless**: Chaque requête contient les infos nécessaires
3. **Cacheable**: Les réponses peuvent être cachées
4. **Uniform Interface**: Utiliser HTTP standards

## 📡 HTTP Methods Flow

```
GET /users/1
  ↓
Read data from database
  ↓
Return 200 + data

POST /users
  ↓
Validate data
  ↓
Create new user
  ↓
Return 201 + created user

PUT /users/1
  ↓
Validate data
  ↓
Replace user completely
  ↓
Return 200 + updated user

PATCH /users/1
  ↓
Validate data
  ↓
Partially update user
  ↓
Return 200 + updated user

DELETE /users/1
  ↓
Delete user
  ↓
Return 204 (No Content)
```

## 📋 HTTP Status Codes Map

```
1xx Informational
  100 Continue
  101 Switching Protocols

2xx Success ✅
  200 OK (GET, PUT, PATCH)
  201 Created (POST)
  202 Accepted (async processing)
  204 No Content (DELETE)

3xx Redirection
  301 Moved Permanently
  302 Found (temporary)
  304 Not Modified (use cache)

4xx Client Error ❌
  400 Bad Request
  401 Unauthorized (not authenticated)
  403 Forbidden (authenticated but no permission)
  404 Not Found
  409 Conflict (duplicate)
  429 Too Many Requests

5xx Server Error 💥
  500 Internal Server Error
  502 Bad Gateway
  503 Service Unavailable
  504 Gateway Timeout
```

## 🛠️ Tools Comparison

| Tool | Purpose | Use Case |
|------|---------|----------|
| **cURL** | Command-line HTTP | Quick testing, scripts |
| **Postman** | GUI client | Interactive testing |
| **Python Requests** | HTTP library | Scripts, automation |
| **http.server** | Simple server | Learning, prototyping |
| **Flask** | Web framework | Production APIs |
| **Django REST** | Full framework | Enterprise APIs |

## 🔐 Authentication Flow

### Basic Auth
```
1. Client sends:
   Authorization: Basic dXNlcjpwYXNz

2. Server decodes:
   user:pass

3. Verify in database
   ✅ Access granted
   ❌ 401 Unauthorized
```

### JWT (Token-based)
```
1. Login
   POST /login
   Body: {username, password}
   ↓
   Return: {access_token: "eyJhbG..."}

2. Use Token
   GET /protected
   Header: Authorization: Bearer eyJhbG...
   ↓
   Verify signature
   ✅ Access granted
   ❌ 401 Unauthorized

3. Token expires
   ⏰ Request new token from /login
```

## 💾 Data Flow in APIs

```
Frontend
  ↓
HTTP Request (JSON)
  ↓
Backend API
  ├─ Parse JSON
  ├─ Validate data
  ├─ Process logic
  ├─ Database query
  └─ Generate response
  ↓
HTTP Response (JSON)
  ↓
Frontend (parse JSON)
```

## 🔄 CRUD Operations

| Operation | Method | URL | Status |
|-----------|--------|-----|--------|
| **Create** | POST | /users | 201 |
| **Read** | GET | /users/1 | 200 |
| **Update** | PUT/PATCH | /users/1 | 200 |
| **Delete** | DELETE | /users/1 | 204 |

## 📝 Request/Response Examples

### Successful GET
```
REQUEST:
GET /posts/1
Host: api.example.com

RESPONSE:
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "title": "Hello",
  "body": "World"
}
```

### Successful POST
```
REQUEST:
POST /posts
Host: api.example.com
Content-Type: application/json

{
  "title": "New Post",
  "body": "Content"
}

RESPONSE:
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 101,
  "title": "New Post",
  "body": "Content",
  "created_at": "2024-01-15"
}
```

### Error Response
```
REQUEST:
GET /posts/9999

RESPONSE:
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "error": "Post not found"
}
```

## 🔗 Common Headers

| Header | Purpose | Example |
|--------|---------|---------|
| **Content-Type** | Data format | application/json |
| **Authorization** | Auth credentials | Bearer token123 |
| **Accept** | Desired response format | application/json |
| **Cache-Control** | Caching policy | max-age=3600 |
| **CORS** | Cross-origin access | * |
| **User-Agent** | Client info | Mozilla/5.0... |
| **X-Custom** | Custom headers | Any value |

## 📚 Code Examples

### cURL
```bash
# GET
curl https://api.example.com/posts

# POST
curl -X POST -H "Content-Type: application/json" \
  -d '{"title":"test"}' \
  https://api.example.com/posts

# With Auth
curl -H "Authorization: Bearer token123" \
  https://api.example.com/protected
```

### Python
```python
import requests

# GET
res = requests.get("https://api.example.com/posts")
data = res.json()

# POST
res = requests.post("https://api.example.com/posts",
                   json={"title": "test"})

# With Auth
headers = {"Authorization": "Bearer token123"}
res = requests.get("https://api.example.com/protected",
                  headers=headers)
```

### Flask
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify([{"id": 1, "title": "Test"}])

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    return jsonify({"message": "Created"}), 201

@app.route("/protected")
@auth.login_required
def protected():
    return "Secret data"
```

## ⚡ Performance Tips

1. **Pagination**: Limiter les résultats
   ```
   GET /posts?page=1&limit=10
   ```

2. **Filtering**: Récupérer seulement ce qu'on a besoin
   ```
   GET /posts?userId=1&status=active
   ```

3. **Sorting**: Ordonner les résultats
   ```
   GET /posts?sort=created_at&order=desc
   ```

4. **Compression**: Compresser les réponses
   ```
   Content-Encoding: gzip
   ```

5. **Caching**: Réutiliser les anciens résultats
   ```
   Cache-Control: max-age=3600
   ```

## 🚨 Common Mistakes

❌ **GET pour modifier**: Utiliser GET pour créer/modifier
✅ POST/PUT/PATCH pour modifier

❌ **Pas de validation**: Accepter n'importe quoi
✅ Valider/nettoyer les entrées

❌ **Pas d'authentification**: APIs publiques
✅ Sécuriser les endpoints sensibles

❌ **Mauvais codes statut**: Toujours 200 OK
✅ Utiliser les codes appropriés (201, 400, 404, etc.)

❌ **Pas de gestion d'erreur**: Crash du serveur
✅ Try/catch et retourner des erreurs JSON

❌ **Secrets codés en dur**: API keys visibles
✅ Utiliser des variables d'environnement

## 🎯 Workflow Complet

```
1. DESIGN
   Définir endpoints, méthodes, réponses

2. IMPLEMENT
   Créer les routes dans Flask/Django

3. VALIDATE
   Vérifier les entrées

4. PROCESS
   Logique métier, DB queries

5. RESPOND
   Retourner les données avec bon code

6. TEST
   cURL, Postman, tests automatisés

7. SECURE
   Auth, validation, rate limiting

8. DOCUMENT
   OpenAPI/Swagger

9. DEPLOY
   Mise en production

10. MONITOR
    Logs, métriques, alertes
```

## 🌟 Best Practices Résumé

```
✅ RESTful Design
  - GET pour lire
  - POST pour créer
  - PUT/PATCH pour modifier
  - DELETE pour supprimer
  - Codes statut appropriés

✅ Security
  - HTTPS obligatoire
  - Authentification/Autorisation
  - Valider les entrées
  - Hacher les mots de passe
  - Rate limiting

✅ Performance
  - Pagination
  - Caching
  - Compression
  - Indexation DB

✅ Documentation
  - OpenAPI/Swagger
  - Exemples clairs
  - Codes d'erreur documentés
  - Authentification expliquée

✅ Testing
  - Tests unitaires
  - Tests d'intégration
  - Tests de charge
  - Tests de sécurité
```

---

Gardez ce cheat sheet près de vous! 📌
