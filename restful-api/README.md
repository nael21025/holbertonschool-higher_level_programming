# RESTful API Learning Project

> Apprendre à construire, consommer et sécuriser les APIs RESTful avec Python

## 📚 Overview

Ce projet couvre les concepts essentiels des APIs RESTful, de la compréhension des basics HTTP à la sécurisation des endpoints avec JWT.

## 📁 Structure du Projet

```
restful-api/
│
├── Task 0: HTTP/HTTPS Basics
│   └── task_00_http_https.md       # Explication HTTP/HTTPS, méthodes, codes de statut
│
├── Task 1: API Consumption (cURL)
│   └── task_01_curl_guide.md       # Guide d'utilisation de cURL avec exemples
│
├── Task 2: Data Processing (Python)
│   ├── task_02_requests.py         # Consommer une API et traiter les données
│   └── main_02_requests.py         # Script de test
│
├── Task 3: Simple HTTP Server
│   └── task_03_http_server.py      # API basique avec http.server
│
├── Task 4: Complete Flask API
│   ├── task_04_flask.py            # API complète avec CRUD
│   └── test_flask.py               # Script de test
│
├── Task 5: Security & Authentication
│   ├── task_05_basic_security.py   # Basic Auth + JWT
│   └── test_security.py            # Script de test
│
└── explanation.md                  # Guide complet A-Z (ce document)
```

## 🎯 Learning Objectives

Après ce projet, vous pourrez:

- ✅ Comprendre HTTP/HTTPS et les méthodes REST
- ✅ Consommer une API avec cURL et Python
- ✅ Créer une API simple avec Python
- ✅ Construire une API complète avec Flask
- ✅ Implémenter l'authentification (Basic Auth + JWT)
- ✅ Sécuriser vos endpoints

## 🚀 Quick Start

### Installations

```bash
# Installer les dépendances
pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended

# Vérifier cURL
curl --version
```

### Task 2: Python Requests

```bash
cd restful-api
python3 main_02_requests.py
```

Cela va:
- Afficher le statut et les titres des posts
- Créer `posts.csv` avec les données

### Task 3: HTTP Server

```bash
python3 task_03_http_server.py
```

Puis dans un autre terminal:
```bash
# Test des endpoints
curl http://localhost:8000/
curl http://localhost:8000/data
curl http://localhost:8000/status
```

### Task 4: Flask API

Terminal 1:
```bash
python3 task_04_flask.py
```

Terminal 2:
```bash
python3 test_flask.py
```

### Task 5: Security

Terminal 1:
```bash
python3 task_05_basic_security.py
```

Terminal 2:
```bash
python3 test_security.py
```

## 📖 Documentation Détaillée

Voir [explanation.md](explanation.md) pour:
- Explications détaillées de chaque task
- Exemples de code
- Bonnes pratiques
- Dépannage

## 🔑 Concepts Clés

### HTTP Methods

| Method | Purpose | Idempotent |
|--------|---------|-----------|
| GET | Récupérer | ✅ |
| POST | Créer | ❌ |
| PUT | Remplacer | ✅ |
| PATCH | Modifier | ❌ |
| DELETE | Supprimer | ✅ |

### Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| 200 | OK | Requête réussie |
| 201 | Created | Ressource créée |
| 400 | Bad Request | Données invalides |
| 401 | Unauthorized | Auth requise |
| 403 | Forbidden | Accès refusé |
| 404 | Not Found | Ressource inexistante |
| 409 | Conflict | Conflit (doublon) |
| 500 | Server Error | Erreur serveur |

### Authentication Methods

1. **Basic Auth**: Username:password en Base64
2. **JWT**: Token self-contained avec signature

## 📝 Examples

### cURL GET
```bash
curl https://jsonplaceholder.typicode.com/posts
```

### cURL POST
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","body":"Content","userId":1}' \
  https://jsonplaceholder.typicode.com/posts
```

### Python Requests
```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
data = response.json()
```

### Flask Route
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data")
def get_data():
    return jsonify({"key": "value"})
```

### JWT Login
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"password"}' \
  http://localhost:5000/login
```

## 🔒 Security Best Practices

- ✅ Toujours utiliser HTTPS en production
- ✅ Valider toutes les entrées
- ✅ Hacher les mots de passe
- ✅ Utiliser des secrets forts
- ✅ Implémenter le rate limiting
- ❌ Ne jamais coder les secrets en dur
- ❌ Ne jamais stocker les mots de passe en clair

## 🧪 Testing

Chaque task a un script de test:

```bash
# Task 2
python3 main_02_requests.py

# Task 4
python3 test_flask.py

# Task 5
python3 test_security.py
```

## 📚 Resources

- [Mozilla - HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [cURL Documentation](https://curl.se/docs/)
- [Requests Library](https://requests.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [JWT Introduction](https://jwt.io/introduction)
- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)

## 🎓 Learning Path

1. Lire la documentation HTTP/HTTPS
2. Pratiquer avec cURL
3. Consommer une API avec Python
4. Créer un serveur simple
5. Construire un API Flask
6. Ajouter la sécurité

**Temps estimé**: 15-20 heures

## 💡 Tips

- Utilisez `curl -I` pour voir uniquement les headers
- Utilisez `python3 -m json.tool` pour pretty-print JSON
- Vérifiez les logs du serveur pour déboguer
- Testez avec des outils comme Postman ou Insomnia
- Lisez les erreurs attentivement!

## ✨ Next Steps

Pour approfondir:
- [ ] Ajouter une vraie base de données
- [ ] Implémenter les migrations
- [ ] Ajouter des tests automatisés
- [ ] Documenter avec OpenAPI/Swagger
- [ ] Déployer en production

---

**Created**: February 19, 2026
**Level**: Beginner to Intermediate
**Duration**: 15-20 hours
