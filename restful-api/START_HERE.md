# 🚀 DÉMARRAGE RAPIDE - START HERE!

## ⚡ 5 Étapes pour Commencer

### Étape 1: Lire l'introduction (5 min)
```bash
📖 Ouvrir: README.md
```

### Étape 2: Installer les dépendances (5 min)
```bash
pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended
```

### Étape 3: Vérifier l'installation (2 min)
```bash
python3 -c "import requests, flask, flask_httpauth, flask_jwt_extended; print('✅ All OK')"
curl --version
```

### Étape 4: Choisir votre chemin
- **Je veux juste comprendre**: Lire `explanation.md`
- **Je veux tester rapidement**: Exécuter `main_02_requests.py`
- **Je veux tout apprendre**: Suivre `SETUP_GUIDE.md`

### Étape 5: C'est parti! 🎯

---

## 📋 Trois Chemins Différents

### 🎓 Chemin Learning (Complet - 20h)
1. Lire `task_00_http_https.md` (HTTP basics)
2. Lire `task_01_curl_guide.md` (cURL)
3. Exécuter `main_02_requests.py` (Python API)
4. Lancer `task_03_http_server.py` (Simple server)
5. Lancer `task_04_flask.py` (Complete API)
6. Lancer `task_05_basic_security.py` (Security)
7. Lire `explanation.md` (Deep dive)

### ⚡ Chemin Quick (Essentiel - 5h)
1. Lire `CHEATSHEET.md` (Concepts clés)
2. Exécuter `main_02_requests.py` (Python API)
3. Lancer `task_04_flask.py` avec test (Flask API)
4. Lancer `task_05_basic_security.py` avec test (Security)

### 🔍 Chemin Reference (Rapide - 30min)
1. Consulter `INDEX.md` (Navigation)
2. Consulter `VISUAL_GUIDE.md` (Diagrammes)
3. Consulter `CHEATSHEET.md` (Résumés)
4. Exécuter un exemple au besoin

---

## 🎯 Par Objectif

### Je veux apprendre HTTP
```bash
📖 task_00_http_https.md
🎥 explanation.md (section Task 0)
📊 VISUAL_GUIDE.md
```

### Je veux utiliser une API (GET data)
```bash
📖 task_01_curl_guide.md
🐍 Exécuter: main_02_requests.py
```

### Je veux créer une API simple
```bash
🔧 Créer: Copier task_04_flask.py et modifier
📚 Référence: explanation.md (section Task 4)
```

### Je veux sécuriser mon API
```bash
🔐 Étudier: task_05_basic_security.py
📖 explanation.md (section Task 5)
🧪 Tester: test_security.py
```

---

## 🧪 Tests Rapides

### Vérifier cURL
```bash
curl --version
curl https://jsonplaceholder.typicode.com/posts/1
```

### Vérifier Python requests
```bash
python3 main_02_requests.py
```

### Vérifier Flask
```bash
# Terminal 1
python3 task_04_flask.py

# Terminal 2
curl http://localhost:5000/
```

### Vérifier Security
```bash
# Terminal 1
python3 task_05_basic_security.py

# Terminal 2
curl -u user1:password http://localhost:5000/basic-protected
```

---

## 📂 Fichiers Essentiels

| Fichier | Objectif | Commande |
|---------|----------|----------|
| `README.md` | 👋 Intro | `Lire` |
| `task_00_http_https.md` | 📖 Concepts | `Lire` |
| `task_01_curl_guide.md` | 🛠️  CLI | `Lire + Pratiquer` |
| `task_02_requests.py` | 🐍 Python | `python3 main_02_requests.py` |
| `task_03_http_server.py` | 🌐 Server | `python3 task_03_http_server.py` |
| `task_04_flask.py` | 🔧 API | `python3 task_04_flask.py` |
| `task_05_basic_security.py` | 🔐 Auth | `python3 task_05_basic_security.py` |

---

## ❌ Pas le temps? (10 min)

1. **Lire** `CHEATSHEET.md`
2. **Exécuter** `python3 main_02_requests.py`
3. **Lancer** `python3 task_04_flask.py`
4. **Tester** `curl http://localhost:5000/status`

Voilà! Vous avez les bases! 🎉

---

## 🆘 Problèmes Courants

### Module not found
```bash
pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended
```

### Port en utilisation
```bash
# Changer le port dans le code
# Ou tuer le processus: kill -9 <PID>
```

### Erreur de connexion
```bash
# S'assurer que le serveur est en cours d'exécution
# Utiliser un autre terminal
```

---

## 📞 Besoin d'aide?

1. **Erreur spécifique?** → Lire `SETUP_GUIDE.md`
2. **Concept vague?** → Lire `explanation.md`
3. **Besoin de rapide?** → Consilter `CHEATSHEET.md`
4. **Visualiser le flux?** → Voir `VISUAL_GUIDE.md`

---

## 🎓 Progression

```
⬜ Installation (5 min)
⬜ Compréhension HTTP (30 min)
⬜ Pratique cURL (30 min)
⬜ Python API (30 min)
⬜ Serveur simple (60 min)
⬜ API complète (60 min)
⬜ Sécurité (60 min)
⬜ Maîtrise complète (20 h)

Durée: Suivez votre rythme! ⏱️
```

---

## ✅ Objectifs Attendus

Après ce projet, vous pourrez:

✅ Comprendre HTTP et REST  
✅ Consommer une API avec cURL  
✅ Consommer une API avec Python  
✅ Créer votre propre API  
✅ Sécuriser une API  
✅ Authentifier les utilisateurs  
✅ Implémenter JWT tokens  
✅ Gérer les erreurs correctement  

---

## 🚀 À Faire Maintenant

1. **Exécuter** `pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended`
2. **Ouvrir** `README.md`
3. **Choisir** votre chemin d'apprentissage
4. **Commencer** maintenant! 💪

---

**Créé**: 19 février 2026
**Pour**: Apprenants en APIs RESTful
**Durée**: 15-20 heures (flexible)

Bonne chance! 🚀
