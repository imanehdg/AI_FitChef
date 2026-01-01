from flask import Flask, render_template, request, redirect, session, jsonify, flash
import sqlite3
import os
from dotenv import load_dotenv  # ← AJOUTE
load_dotenv()
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from groq import Groq
from mistralai import Mistral
import json
from datetime import datetime, timedelta
import random
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "users.db")

# Configuration Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# Dictionnaire de synonymes pour la détection d'ingrédients (fallback)
synonymes = {
    "tomato": ["tomate", "tomato", "tomatoes"],
    "egg": ["oeuf", "egg", "eggs"],
    "milk": ["lait", "milk"],
    "cheese": ["fromage", "cheese"],
    "chicken": ["poulet", "chicken"],
    "carrot": ["carotte", "carrot"],
    "cucumber": ["concombre", "cucumber"],
    "quinoa": ["quinoa"],
    "olive oil": ["huile d'olive", "olive oil"],
    "pasta": ["pâtes", "pasta"]
}

# DONNÉES MOTIVATION
QUOTES = [
    {"text": "Le succès, c'est la somme de petits efforts répétés jour après jour", "author": "Robert Collier"},
    {"text": "La seule façon d'échouer, c'est d'abandonner", "author": "Albert Einstein"},
    {"text": "Ton corps peut tout faire. C'est ton esprit qu'il faut convaincre", "author": "Anonyme"},
    {"text": "Ne compte pas les jours, fais que les jours comptent", "author": "Muhammad Ali"},
    {"text": "La discipline est le pont entre les objectifs et l'accomplissement", "author": "Jim Rohn"},
    {"text": "Chaque expert a d'abord été un débutant", "author": "Robin Sharma"},
    {"text": "La motivation te fait commencer. L'habitude te fait continuer", "author": "Jim Ryun"},
    {"text": "Le meilleur moment pour planter un arbre était il y a 20 ans. Le deuxième meilleur moment, c'est maintenant", "author": "Proverbe chinois"},
    {"text": "Tu n'as pas besoin d'être excellent pour commencer, mais tu dois commencer pour devenir excellent", "author": "Zig Ziglar"},
    {"text": "Transforme ton 'je ne peux pas' en 'je vais essayer'", "author": "Anonyme"}
]

CHALLENGES = [
    "Bois <strong>2 litres d'eau</strong> aujourd'hui et fais <strong>30 minutes de marche</strong> !",
    "Mange <strong>5 portions de fruits et légumes</strong> et évite les sucreries !",
    "Fais <strong>20 squats</strong> le matin et <strong>20 le soir</strong> !",
    "Prends <strong>10 000 pas</strong> aujourd'hui et bois un smoothie vert !",
    "Pas d'écrans <strong>1h avant le coucher</strong> et dors <strong>8 heures</strong> !",
    "Prépare <strong>tous tes repas maison</strong> aujourd'hui, zéro fast-food !",
    "Fais <strong>15 minutes de yoga</strong> le matin et médite <strong>5 minutes</strong> !",
    "Cuisine <strong>une nouvelle recette saine</strong> et partage-la avec quelqu'un !"
]

TIPS = [
    {"emoji": "💧", "text": "Commence ta journée avec un grand verre d'eau au réveil"},
    {"emoji": "🥗", "text": "Ajoute des légumes colorés à chaque repas"},
    {"emoji": "⏰", "text": "Mange ton dernier repas 3h avant de dormir"},
    {"emoji": "🏃", "text": "Marche 10 minutes après chaque repas"},
    {"emoji": "😴", "text": "Dors 7-8 heures pour une récupération optimale"},
    {"emoji": "📝", "text": "Note ce que tu manges pour mieux t'organiser"},
    {"emoji": "🍎", "text": "Privilégie les fruits entiers plutôt que les jus"},
    {"emoji": "🥜", "text": "Ajoute des noix ou amandes à tes collations"},
    {"emoji": "🍳", "text": "Prends un petit-déjeuner riche en protéines"},
    {"emoji": "🥤", "text": "Évite les boissons sucrées et sodas"},
    {"emoji": "🧘", "text": "Prends le temps de manger lentement et consciemment"},
    {"emoji": "🥦", "text": "Intègre des légumes verts à feuilles chaque jour"}
]

def detect_food_with_ai(image_path):
    """Détecte les ingrédients avec Mistral Pixtral"""
    try:
        print(f"🔍 Analyse de l'image avec Mistral: {image_path}")

        # Encoder l'image en base64
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        print("📸 Image encodée, appel à Mistral Pixtral...")

        # Créer le client Mistral
        client_mistral = Mistral(api_key="YbBI0kvd38l7REOvDfjZI2ulFKSqwZ70")

        # Appel à Mistral Pixtral
        chat_response = client_mistral.chat.complete(
            model="pixtral-12b-2409",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Analyse cette image et liste TOUS les aliments visibles.

INSTRUCTIONS:
- Liste les noms des aliments en français
- Sépare-les par des virgules
- Noms simples (ex: "tomate" pas "tomate rouge")
- AUCUNE explication, juste la liste
- Si aucun aliment, réponds "aucun"

EXEMPLE: tomate, carotte, poivron, concombre, laitue, jambon"""
                        },
                        {
                            "type": "image_url",
                            "image_url": f"data:image/jpeg;base64,{image_data}"
                        }
                    ]
                }
            ]
        )

        response = chat_response.choices[0].message.content.strip()
        print(f"🤖 Mistral a répondu: {response}")

        # Nettoyer la réponse
        if "aucun" in response.lower():
            return []

        # Enlever les explications si présentes
        if ":" in response:
            response = response.split(":")[-1]

        # Convertir en liste
        detected = []
        for item in response.split(","):
            item = item.strip().lower()
            item = item.replace(".", "").replace("!", "").replace("?", "")
            if item and len(item) > 2:
                detected.append(item)

        print(f"✅ Ingrédients détectés: {detected}")
        return detected

    except Exception as e:
        print(f"❌ Erreur Mistral: {e}")
        import traceback
        traceback.print_exc()
        return detect_food_mock(image_path)

def detect_food_mock(img_path):
    """Détection basique par nom de fichier (fallback)"""
    detected = []
    filename = os.path.basename(img_path).lower()
    for key, mots in synonymes.items():
        for mot in mots:
            if mot in filename and key not in detected:
                detected.append(key)
    return detected

# Flask config
app = Flask(__name__)
app.secret_key = "une_clef_secrete_a_changer"

UPLOAD_FOLDER = os.path.join("static", "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def init_motivation_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS UserMotivation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            streak_count INTEGER DEFAULT 1,
            last_activity_date TEXT,
            current_challenge TEXT,
            challenge_progress INTEGER DEFAULT 0,
            challenge_completed INTEGER DEFAULT 0,
            challenge_date TEXT,
            total_challenges_completed INTEGER DEFAULT 0,
            best_streak INTEGER DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Table UserMotivation créée/vérifiée")

init_motivation_table()

def get_or_create_motivation(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM UserMotivation WHERE username=?", (username,))
    motivation = c.fetchone()
    if not motivation:
        today = datetime.now().date().isoformat()
        challenge = random.choice(CHALLENGES)
        c.execute('''
            INSERT INTO UserMotivation
            (username, streak_count, last_activity_date, current_challenge,
             challenge_date, challenge_progress, challenge_completed)
            VALUES (?, 1, ?, ?, ?, 0, 0)
        ''', (username, today, challenge, today))
        conn.commit()
        c.execute("SELECT * FROM UserMotivation WHERE username=?", (username,))
        motivation = c.fetchone()
    conn.close()
    return motivation

def update_streak(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT streak_count, last_activity_date, best_streak FROM UserMotivation WHERE username=?", (username,))
    data = c.fetchone()
    if not data:
        conn.close()
        return
    streak_count, last_activity, best_streak = data
    today = datetime.now().date()
    last_date = datetime.fromisoformat(last_activity).date() if last_activity else today
    if last_date == today:
        conn.close()
        return streak_count
    yesterday = today - timedelta(days=1)
    if last_date == yesterday:
        streak_count += 1
    elif last_date < yesterday:
        streak_count = 1
    if streak_count > best_streak:
        best_streak = streak_count
    c.execute('''
        UPDATE UserMotivation
        SET streak_count=?, last_activity_date=?, best_streak=?, updated_at=?
        WHERE username=?
    ''', (streak_count, today.isoformat(), best_streak, datetime.now().isoformat(), username))
    conn.commit()
    conn.close()
    return streak_count

def reset_daily_challenge(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT challenge_date, current_challenge FROM UserMotivation WHERE username=?", (username,))
    data = c.fetchone()
    if not data:
        conn.close()
        return
    challenge_date, current_challenge = data
    today = datetime.now().date()
    if challenge_date:
        last_challenge_date = datetime.fromisoformat(challenge_date).date()
        if last_challenge_date < today:
            new_challenge = random.choice(CHALLENGES)
            c.execute('''
                UPDATE UserMotivation
                SET challenge_completed=0, challenge_progress=0,
                    challenge_date=?, current_challenge=?
                WHERE username=?
            ''', (today.isoformat(), new_challenge, username))
            conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        taille = float(request.form["taille"])
        poids = float(request.form["poids"])
        objectif = request.form["objectif"]
        activite = request.form["activite"]
        hashed_password = generate_password_hash(password)
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO Users (username, password, taille, poids, objectif, activite) VALUES (?, ?, ?, ?, ?, ?)",
            (username, hashed_password, taille, poids, objectif, activite))
        conn.commit()
        conn.close()
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM Users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()
        if user and check_password_hash(user[2], password):
            session["username"] = username
            return redirect("/profile")
        elif user:
            return "Mot de passe incorrect"
        else:
            return "Nom incorrect"
    return render_template("login.html")

@app.route("/profile")
def profile():
    if "username" not in session:
        return redirect("/login")
    username = session["username"]
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT taille, poids, objectif, activite FROM Users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    if not user:
        return "Utilisateur introuvable"
    taille, poids, objectif, activite = user
    imc = round(poids / (taille / 100) ** 2, 2)
    calories = 1800 if activite == "sedentaire" else 2100 if activite == "moyenne" else 2400
    return render_template("profile.html", username=username, taille=taille, poids=poids, objectif=objectif, activite=activite, imc=imc, calories=calories)

@app.route("/recettes")
def recettes():
    if "username" not in session:
        return redirect("/login")
    username = session["username"]
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT objectif FROM Users WHERE username=?", (username,))
    row = c.fetchone()
    if not row or not row[0]:
        conn.close()
        return render_template("recettes.html", username=username, recettes=[], objectif="être en forme")
    objectif = row[0]
    c.execute("SELECT nom, ingredients, instructions, temps, calories, photo FROM Recettes WHERE objectif=?", (objectif,))
    recettes_list = c.fetchall()
    conn.close()
    recettes_dict = []
    for r in recettes_list:
        recettes_dict.append({"nom": r[0], "ingredients": r[1] if r[1] else "Aucun ingrédient",
            "instructions": r[2] if r[2] else "Aucune instruction", "temps": r[3] if len(r) > 3 and r[3] else 20,
            "calories": r[4] if len(r) > 4 and r[4] else 400, "photo": r[5] if len(r) > 5 else None})
    return render_template("recettes.html", username=username, recettes=recettes_dict, objectif=objectif)

@app.route("/recette/<nom>")
def recette_detail(nom):
    if "username" not in session:
        return redirect("/login")
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT nom, ingredients, instructions, temps, calories, photo FROM Recettes WHERE nom=?", (nom,))
    recette = c.fetchone()
    conn.close()
    if not recette:
        return "Recette introuvable"
    return render_template("recette_detail.html", nom=recette[0], ingredients=recette[1] if recette[1] else "Aucun ingrédient",
        instructions=recette[2] if recette[2] else "Aucune instruction", temps=recette[3] if recette[3] else 20,
        calories=recette[4] if recette[4] else 400, photo=recette[5] if len(recette) > 5 else None)

@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    if "username" not in session:
        return redirect("/login")
    username = session["username"]
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if request.method == "POST":
        taille = float(request.form["taille"])
        poids = float(request.form["poids"])
        objectif = request.form["objectif"]
        activite = request.form["activite"]
        c.execute("UPDATE Users SET taille=?, poids=?, objectif=?, activite=? WHERE username=?",
            (taille, poids, objectif, activite, username))
        conn.commit()
        conn.close()
        return redirect("/profile")
    c.execute("SELECT taille, poids, objectif, activite FROM Users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return render_template("edit_profile.html", username=username, taille=user[0], poids=user[1], objectif=user[2], activite=user[3])

@app.route("/frigo", methods=["GET", "POST"])
def frigo():
    if "username" not in session:
        return redirect("/login")
    username = session["username"]

    if request.method == "POST":
        if "image" not in request.files or request.files["image"].filename == "":
            return "Aucun fichier sélectionné", 400

        file = request.files["image"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)

            print(f"📁 Fichier sauvegardé: {save_path}")

            # Détection avec IA
            detected = detect_food_with_ai(save_path)
            print(f"✅ Détection finale: {detected}")

            # Recherche des recettes correspondantes
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()

            # Récupérer toutes les recettes avec temps et calories
            c.execute("SELECT nom, ingredients, instructions, temps, calories FROM Recettes")
            all_recipes = c.fetchall()

            matches = []
            for r in all_recipes:
                nom, ingredients, instructions, temps, calories = r
                recette_ing = [i.strip().lower() for i in ingredients.split(",")] if ingredients else []

                # Compter les ingrédients détectés
                count_detected = 0
                for ing in recette_ing:
                    for detected_item in detected:
                        # Comparaison flexible (contient ou est contenu)
                        if detected_item in ing or ing in detected_item:
                            count_detected += 1
                            break

                missing = len(recette_ing) - count_detected

                # N'ajouter QUE si au moins 1 ingrédient match
                if count_detected > 0:
                    matches.append({
                        "nom": nom,
                        "ingredients": ingredients if ingredients else "Aucun ingrédient",
                        "instructions": instructions if instructions else "Aucune instruction",
                        "temps": temps if temps else 30,
                        "calories": calories if calories else 400,
                        "missing": missing,
                        "match_count": count_detected,
                        "compatible": missing == 0
                    })

            # Trier par nombre d'ingrédients matchés (du + au -)
            matches.sort(key=lambda x: (-x["match_count"], x["missing"]))

            conn.close()

            print(f"🍽️ {len(matches)} recettes trouvées")

            return render_template("frigo_result.html",
                username=username,
                detected=detected if detected else [],
                recipes=matches,
                image_url="/" + save_path.replace("\\", "/"))

        return "Type de fichier non autorisé", 400

    return render_template("frigo.html", username=username)

@app.route("/planning")
def planning():
    if "username" not in session:
        return redirect("/login")
    username = session["username"]
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT objectif FROM Users WHERE username=?", (username,))
    row = c.fetchone()
    conn.close()
    objectif = row[0] if row and row[0] else "être en forme"
    return render_template("planning.html", username=username, objectif=objectif)

def calculer_calories(poids, taille, age, niveau_activite, objectif):
    bmr = 10 * poids + 6.25 * taille - 5 * age + 5
    facteurs = {'sedentaire': 1.2, 'leger': 1.375, 'moyen': 1.55, 'moyenne': 1.55, 'intense': 1.725, 'tres_intense': 1.9}
    facteur = facteurs.get(niveau_activite.lower(), 1.55)
    calories_totales = bmr * facteur
    objectif_lower = objectif.lower()
    if 'perte' in objectif_lower or 'maigrir' in objectif_lower:
        calories_totales -= 500
    elif 'prise' in objectif_lower or 'masse' in objectif_lower:
        calories_totales += 500
    return int(calories_totales)

@app.route('/api/generate_planning', methods=['POST'])
def generate_planning():
    if "username" not in session:
        return jsonify({'success': False, 'error': 'Non connecté'}), 401
    try:
        username = session["username"]
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT taille, poids, objectif, activite FROM Users WHERE username=?", (username,))
        user = c.fetchone()
        conn.close()
        if not user:
            return jsonify({'success': False, 'error': 'Utilisateur introuvable'}), 404
        taille, poids, objectif, activite = user
        age = 30
        calories_quotidiennes = calculer_calories(poids, taille, age, activite, objectif)
        prompt = f"""Tu es un nutritionniste expert. Crée un planning alimentaire pour 7 jours.
PROFIL: Objectif: {objectif}, Calories/jour: {calories_quotidiennes} kcal, Poids: {poids} kg, Taille: {taille} cm
STRUCTURE JSON (SANS MARKDOWN):
{{"lundi": {{"petit_dejeuner": {{"nom": "Nom", "description": "Ingrédients", "calories": 400}}, "snack_matin": {{"nom": "Nom", "description": "Ingrédients", "calories": 150}}, "dejeuner": {{"nom": "Nom", "description": "Ingrédients", "calories": 500}}, "snack_apres_midi": {{"nom": "Nom", "description": "Ingrédients", "calories": 150}}, "diner": {{"nom": "Nom", "description": "Ingrédients", "calories": 450}}}}, "mardi": {{...}}, "mercredi": {{...}}, "jeudi": {{...}}, "vendredi": {{...}}, "samedi": {{...}}, "dimanche": {{...}}}}
Réponds UNIQUEMENT avec le JSON."""
        chat_completion = client.chat.completions.create(
            messages=[{"role": "system", "content": "Tu réponds UNIQUEMENT en JSON, sans markdown."},
                {"role": "user", "content": prompt}], model="llama-3.3-70b-versatile", temperature=0.7, max_tokens=4000)
        response_text = chat_completion.choices[0].message.content.strip()
        if response_text.startswith('```json'):
            response_text = response_text[7:]
        if response_text.startswith('```'):
            response_text = response_text[3:]
        if response_text.endswith('```'):
            response_text = response_text[:-3]
        response_text = response_text.strip()
        planning_data = json.loads(response_text)
        return jsonify({'success': True, 'planning': planning_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/motivation')
def motivation():
    if 'username' not in session:
        return redirect('/login')
    username = session['username']
    motivation_data = get_or_create_motivation(username)
    reset_daily_challenge(username)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM UserMotivation WHERE username=?", (username,))
    data = c.fetchone()
    conn.close()
    if not data:
        return "Erreur de données", 500
    random_quote = random.choice(QUOTES)
    random_tips = random.sample(TIPS, 6)
    return render_template('motivation.html', username=username, streak=data[2], best_streak=data[9],
        challenge=data[4], progress=data[5], completed=bool(data[6]), total_completed=data[8], quote=random_quote, tips=random_tips)

@app.route('/api/motivation/update-progress', methods=['POST'])
def update_progress():
    print("🔥 update-progress appelée !")
    if 'username' not in session:
        print("❌ Pas de session")
        return jsonify({'success': False, 'message': 'Non connecté'}), 401
    username = session['username']
    print(f"✅ Username: {username}")
    try:
        data = request.get_json()
        print(f"📦 Data reçue: {data}")
        progress = min(int(data.get('progress', 0)), 100)
        print(f"📊 Progress: {progress}")
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("UPDATE UserMotivation SET challenge_progress=? WHERE username=?", (progress, username))
        print(f"✏️ Lignes modifiées: {c.rowcount}")
        if progress >= 100:
            print("🎉 Progress = 100%, mise à jour streak...")
            update_streak(username)
            c.execute('''UPDATE UserMotivation SET challenge_completed=1, total_challenges_completed=total_challenges_completed+1
                WHERE username=? AND challenge_completed=0''', (username,))
        conn.commit()
        c.execute("SELECT streak_count, challenge_completed FROM UserMotivation WHERE username=?", (username,))
        result = c.fetchone()
        print(f"📈 Résultat: {result}")
        conn.close()
        return jsonify({'success': True, 'progress': progress, 'streak': result[0] if result else 1,
            'completed': bool(result[1]) if result else False})
    except Exception as e:
        print(f"❌ ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/motivation/complete-challenge', methods=['POST'])
def complete_challenge():
    print("🔥 complete-challenge appelée !")
    if 'username' not in session:
        print("❌ Pas de session")
        return jsonify({'success': False, 'message': 'Non connecté'}), 401
    username = session['username']
    print(f"✅ Username: {username}")
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT challenge_completed FROM UserMotivation WHERE username=?", (username,))
        data = c.fetchone()
        print(f"📊 Challenge déjà complété ? {data}")
        if data and data[0] == 1:
            conn.close()
            print("⚠️ Déjà complété")
            return jsonify({'success': False, 'message': 'Déjà complété aujourd\'hui'}), 400
        print("✏️ Mise à jour du challenge...")
        new_streak = update_streak(username)
        c.execute('''UPDATE UserMotivation SET challenge_completed=1, challenge_progress=100,
            total_challenges_completed=total_challenges_completed+1 WHERE username=?''', (username,))
        print(f"✏️ Lignes modifiées: {c.rowcount}")
        conn.commit()
        c.execute("SELECT streak_count, total_challenges_completed FROM UserMotivation WHERE username=?", (username,))
        result = c.fetchone()
        print(f"📈 Résultat: {result}")
        conn.close()
        return jsonify({'success': True, 'message': '🎉 Challenge complété !',
            'streak': result[0] if result else 1, 'total_completed': result[1] if result else 1})
    except Exception as e:
        print(f"❌ ERREUR: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'success': False, 'error': 'Message vide'}), 400

        print(f"💬 Message reçu: {user_message}")

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """Tu es FitChef IA, un coach nutrition bienveillant et expert en français.

🎯 TON RÔLE:
- Réponds de manière concise et amicale (2-4 phrases max)
- Utilise des emojis pour rendre la conversation agréable (🥗🏃💪🎯💧🍎)
- Sois encourageant et positif
- Donne des conseils pratiques et réalistes

📚 TES DOMAINES D'EXPERTISE:
- Nutrition et alimentation saine
- Idées de recettes équilibrées et savoureuses
- Conseils pour atteindre des objectifs (perte/prise de poids, fitness)
- Motivation et habitudes saines
- Questions sur les calories, macros, portions

✨ TON STYLE:
- Phrases courtes et claires
- Ton chaleureux et motivant
- Évite le jargon médical compliqué
- Adapte-toi à la personne (encourage, motive)
- Si on te demande des recettes, donne 2-3 suggestions avec détails

⚠️ LIMITES:
- Tu ne remplaces pas un médecin ou nutritionniste professionnel
- Pour des problèmes de santé graves, recommande de consulter un expert"""
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.8,
            max_tokens=600
        )

        bot_response = chat_completion.choices[0].message.content.strip()
        print(f"🤖 Réponse générée: {bot_response[:100]}...")

        return jsonify({
            'success': True,
            'response': bot_response
        })

    except Exception as e:
        print(f"❌ ERREUR CHATBOT: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Désolé, je ne peux pas répondre pour le moment 😔'
        }), 500

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        message = request.form.get('message', '').strip()
        if not name or not email or not message:
            flash('Tous les champs obligatoires doivent être remplis', 'error')
            return redirect('/contact')
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS ContactMessages (
                id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL,
                phone TEXT, message TEXT NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
            c.execute('INSERT INTO ContactMessages (name, email, phone, message) VALUES (?, ?, ?, ?)', (name, email, phone, message))
            conn.commit()
            conn.close()
            flash('✅ Message envoyé avec succès ! Nous vous répondrons bientôt.', 'success')
            return redirect('/contact')
        except Exception as e:
            flash('❌ Erreur lors de l\'envoi du message', 'error')
            return redirect('/contact')
    return render_template('contact.html')

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)