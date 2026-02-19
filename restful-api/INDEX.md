# 📚 Index Complet du Projet RESTful API

## 🎯 Par Ordre d'Apprentissage

### 1️⃣ [README.md](README.md) - **COMMENCER ICI**
Présentation générale du projet, objectifs et quick start

### 2️⃣ Task 0: Fondamentaux HTTP/HTTPS
- **Document**: [task_00_http_https.md](task_00_http_https.md)
- **Contenu**:
  - ✅ Différences HTTP vs HTTPS
  - ✅ Structure requête/réponse
  - ✅ Les 7 méthodes HTTP
  - ✅ Les codes de statut 1xx à 5xx
- **Temps**: 30-45 minutes
- **Action**: Lire attentivement

### 3️⃣ Task 1: cURL - Consommer une API
- **Document**: [task_01_curl_guide.md](task_01_curl_guide.md)
- **Contenu**:
  - ✅ Installation de cURL
  - ✅ Syntaxe et flags principaux
  - ✅ GET, POST, PUT, DELETE avec cURL
  - ✅ Authentification et headers
  - ✅ JSONPlaceholder exemples
- **Temps**: 45-60 minutes
- **Action**: Lire + pratiquer avec cURL

### 4️⃣ Task 2: Python Requests
- **Fichier Code**: [task_02_requests.py](task_02_requests.py)
- **Fichier Test**: [main_02_requests.py](main_02_requests.py)
- **Contenu**:
  - ✅ Requêtes GET avec requests
  - ✅ Parsing JSON
  - ✅ Export CSV
  - ✅ Gestion d'erreurs
- **Temps**: 30-45 minutes
- **Action**: Lancer et tester
  ```bash
  python3 main_02_requests.py
  ```
- **Sortie**: `posts.csv` généré

### 5️⃣ Task 3: Serveur HTTP Simple
- **Fichier Code**: [task_03_http_server.py](task_03_http_server.py)
- **Contenu**:
  - ✅ Créer un serveur HTTP basique
  - ✅ Handler personnalisé
  - ✅ GET avec routes
  - ✅ Réponses JSON
  - ✅ Gestion des 404
- **Temps**: 45-60 minutes
- **Action**: Lancer et tester
  ```bash
  python3 task_03_http_server.py
  # Test: curl http://localhost:8000/
  ```

### 6️⃣ Task 4: API Complète avec Flask
- **Fichier Code**: [task_04_flask.py](task_04_flask.py)
- **Fichier Test**: [test_flask.py](test_flask.py)
- **Contenu**:
  - ✅ Routes Flask avec @app.route()
  - ✅ GET, POST, PUT, DELETE
  - ✅ Paramètres dynamiques
  - ✅ Validation d'entrée
  - ✅ Stockage en mémoire
  - ✅ Codes de statut appropriés
- **Temps**: 60-90 minutes
- **Action**: Lancer et tester
  ```bash
  python3 task_04_flask.py  # Terminal 1
  python3 test_flask.py     # Terminal 2
  ```

### 7️⃣ Task 5: Sécurité et Authentification
- **Fichier Code**: [task_05_basic_security.py](task_05_basic_security.py)
- **Fichier Test**: [test_security.py](test_security.py)
- **Contenu**:
  - ✅ Basic Authentication (HTTP)
  - ✅ JWT Tokens
  - ✅ Login endpoint
  - ✅ Protection des routes
  - ✅ Contrôle d'accès par rôle (RBAC)
  - ✅ Gestion des erreurs JWT
  - ✅ Hachage des mots de passe
- **Temps**: 90-120 minutes
- **Action**: Lancer et tester
  ```bash
  python3 task_05_basic_security.py  # Terminal 1
  python3 test_security.py           # Terminal 2
  ```

---

## 📖 Guides Supplémentaires

### [explanation.md](explanation.md) - **GUIDE COMPLET A-Z**
Explication détaillée de chaque concept avec:
- 📝 Explications textuelles
- 💻 Examples de code
- 📊 Diagrammes ASCII
- 🔍 Analyses en profondeur
- 🎯 Cas d'usage réels
- ⚠️ Pièges courants

**Parcourez par section**:
- Introduction aux APIs
- Task 0: HTTP/HTTPS Basics
- Task 1: cURL Guide
- Task 2: Python Requests
- Task 3: http.server
- Task 4: Flask
- Task 5: Sécurité

### [CHEATSHEET.md](CHEATSHEET.md) - **RÉFÉRENCE RAPIDE**
Résumé visuel des concepts clés:
- 🔄 Flow diagrams
- 📋 Tableaux récapitulatifs
- 📱 HTTP Methods map
- 📊 Status codes map
- 🔐 Authentication flows
- 💾 CRUD operations
- ⚡ Performance tips
- 🚨 Common mistakes

### [SETUP_GUIDE.md](SETUP_GUIDE.md) - **LANCER LES EXERCICES**
Instructions pas-à-pas pour chaque task:
- 🔧 Installations
- 🚀 Commandes de lancement
- 📤 Sorties attendues
- 🧪 Tests manuels avec cURL
- ✅ Checklist

---

## 🗂️ Structure des Fichiers

```
restful-api/
│
├── 📖 DOCUMENTATION
│   ├── README.md                    # Vue d'ensemble (DÉMARRER ICI)
│   ├── explanation.md               # Guide complet A-Z
│   ├── CHEATSHEET.md               # Référence rapide
│   ├── SETUP_GUIDE.md              # Instructions de lancement
│   └── INDEX.md                    # Ce fichier
│
├── 🎓 TASK 0: HTTP/HTTPS
│   └── task_00_http_https.md       # Documentation
│
├── 📡 TASK 1: cURL
│   └── task_01_curl_guide.md       # Guide + exemples
│
├── 🐍 TASK 2: Python Requests
│   ├── task_02_requests.py         # Code principal
│   ├── main_02_requests.py         # Lanceur
│   └── posts.csv                   # Output généré
│
├── 🌐 TASK 3: HTTP Server
│   └── task_03_http_server.py      # Serveur simple
│
├── 🔧 TASK 4: Flask API
│   ├── task_04_flask.py            # API Flask
│   └── test_flask.py               # Tests
│
└── 🔐 TASK 5: Sécurité
    ├── task_05_basic_security.py   # API sécurisée
    └── test_security.py            # Tests
```

---

## 🚀 Quick Navigation

### Je veux apprendre...

**les basics HTTP**
→ Lirr [task_00_http_https.md](task_00_http_https.md)

**à utiliser cURL**
→ Lire [task_01_curl_guide.md](task_01_curl_guide.md) + pratiquer

**à consommer une API en Python**
→ Exécuter [main_02_requests.py](main_02_requests.py)

**à créer un serveur simple**
→ Exécuter [task_03_http_server.py](task_03_http_server.py)

**à créer une API complète**
→ Exécuter [task_04_flask.py](task_04_flask.py) + [test_flask.py](test_flask.py)

**à sécuriser une API**
→ Exécuter [task_05_basic_security.py](task_05_basic_security.py) + [test_security.py](test_security.py)

**tout rapidement**
→ Lire [CHEATSHEET.md](CHEATSHEET.md)

**avec détails complets**
→ Lire [explanation.md](explanation.md)

**comment démarrer chaque task**
→ Voir [SETUP_GUIDE.md](SETUP_GUIDE.md)

---

## 📊 Progression

```
█████░░░░░░░░░░░░░░░░ Task 0: HTTP/HTTPS (conceptuel)
██████████░░░░░░░░░░░░░░░░░░░░░░ Task 1: cURL (cli)
████████████████░░░░░░░░░░░░░░░░░░░░░░░░ Task 2: Python (simple)
██████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░ Task 3: http.server (basique)
████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ Task 4: Flask (complet)
██████████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ Task 5: Sécurité (avancé)

Temps total: 15-20 heures
```

---

## 🎯 Objectifs par Task

| Task | Objectif | Résultat |
|------|----------|----------|
| 0 | Comprendre HTTP/HTTPS | Knowledge ✅ |
| 1 | Tester une API en ligne | Expérience ✅ |
| 2 | Consommer une API en Python | Script fonctionnel ✅ |
| 3 | Créer un serveur simple | Serveur opérationnel ✅ |
| 4 | Créer une API complète | API CRUD complète ✅ |
| 5 | Sécuriser une API | Auth + JWT ✅ |

---

## 🔑 Technologies Couvertes

- **HTTP/HTTPS**: Protocoles web
- **cURL**: Client pour requêtes HTTP
- **Python**: Langage de programmation
- **requests**: Librairie HTTP Python
- **http.server**: Module serveur standard Python
- **Flask**: Framework web léger
- **Flask-HTTPAuth**: Basic Auth
- **Flask-JWT-Extended**: JWT tokens
- **JSON**: Format d'échange de données
- **CSV**: Format de données tabulaires

---

## 📚 Ressources Externes

| Ressource | Lien |
|-----------|------|
| HTTP MDN | https://developer.mozilla.org/en-US/docs/Web/HTTP |
| cURL Tutorial | https://curl.se/docs/manual.html |
| Python Requests | https://requests.readthedocs.io/ |
| Flask Docs | https://flask.palletsprojects.com/ |
| JWT | https://jwt.io/ |
| JSONPlaceholder | https://jsonplaceholder.typicode.com/ |

---

## ⚡ Commandes Les Plus Utiles

```bash
# Installer les dépendances
pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended

# Task 2: Exécuter
python3 main_02_requests.py

# Task 3: Serveur
python3 task_03_http_server.py
curl http://localhost:8000/data

# Task 4: Flask
python3 task_04_flask.py  # Terminal 1
python3 test_flask.py     # Terminal 2

# Task 5: Sécurité
python3 task_05_basic_security.py  # Terminal 1
python3 test_security.py           # Terminal 2
```

---

## ✅ Checklist d'Apprentissage

- [ ] Lire README.md
- [ ] Lire task_00_http_https.md
- [ ] Pratiquer cURL
- [ ] Exécuter main_02_requests.py
- [ ] Lancer et tester task_03_http_server.py
- [ ] Lancer et tester task_04_flask.py
- [ ] Lancer et tester task_05_basic_security.py
- [ ] Relire explanation.md pour approfondir
- [ ] Créer ma propre API (bonus)
- [ ] Déployer en production (bonus)

---

## 🎓 Prochain Cours Recommandé

- [ ] **Bases de données**: SQLite, PostgreSQL avec SQLAlchemy
- [ ] **Migrations**: Alembic pour versionner le schéma DB
- [ ] **Testing**: pytest pour tester les APIs
- [ ] **Documentation**: OpenAPI/Swagger
- [ ] **Déploiement**: Docker, Heroku, AWS

---

**Créé par**: Équipe pédagogique
**Date**: 19 février 2026
**Niveau**: Débutant → Intermédiaire
**Durée**: 15-20 heures

---

## 💡 Pro Tips

1. **Faites pause entre les tasks** - Chaque concept prend du temps à s'installer
2. **Pratiquez avec vos propres APIs** - Testez avec GitHub API, OpenWeather, etc.
3. **Lisez les codes d'erreur** - Ils vous disent souvent exactement ce qui ne va pas
4. **Documentez votre code** - Les APIs doivent être claires
5. **Testez tout** - Écrire des tests vous sauve temps plus tard

---

**Bon apprentissage!** 🚀
