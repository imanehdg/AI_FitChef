# AI FitChef 🍳

Application web de nutrition intelligente utilisant l'IA pour détecter les ingrédients et générer des recettes personnalisées.

## 🚀 Démonstration en ligne
https://imanehdg.pythonanywhere.com/

## 📋 Prérequis
- Python 3.10+
- Flask
- SQLite3
- Clés API : Groq et Mistral AI

## 🔧 Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/imanehdg/AI_FitChef.git
cd AI_FitChef
```

2. Créer un environnement virtuel :
```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installer les dépendances :
```bash
pip install flask python-dotenv werkzeug groq mistralai
```

4. Créer un fichier `.env` à la racine :
```
GROQ_API_KEY=votre_clé_groq
MISTRAL_API_KEY=votre_clé_mistral
```

5. Initialiser la base de données :
```bash
python3 create_db.py
```

6. Lancer l'application :
```bash
python3 app.py
```

7. Ouvrir dans le navigateur : http://localhost:5000

## 📁 Structure du projet
```
AI_FitChef/
├── app.py                      # Application principale Flask
├── database/                   # Base de données SQLite
├── static/                     # Fichiers CSS, JS, images
├── templates/                  # Templates HTML
├── create_db.py               # Script d'initialisation DB
├── rapport/                   # Documentation du projet
└── README.md
```

## 🛠️ Technologies utilisées
- **Backend** : Flask (Python)
- **Base de données** : SQLite
- **IA** : Groq API, Mistral AI
- **Frontend** : HTML, CSS, JavaScript
- **Hébergement** : PythonAnywhere

## 👥 Auteur
Imane HADDAG et Sarah TAMANI

