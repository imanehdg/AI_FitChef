import sqlite3
import os

# crée le dossier database s'il n'existe pas
os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/users.db")
c = conn.cursor()

# Table Users
c.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    taille REAL,
    poids REAL,
    objectif TEXT,
    activite TEXT
)
""")

# Table Recettes (nom, objectif, ingredients, instructions, calories)
c.execute("""
CREATE TABLE IF NOT EXISTS Recettes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE,
    objectif TEXT,
    ingredients TEXT,
    instructions TEXT,
    calories INTEGER
)
""")

# Insère quelques recettes tests (si la table est vide)
c.execute("SELECT COUNT(*) FROM Recettes")
count = c.fetchone()[0]
if count == 0:
    recettes = [
        ("Salade de quinoa et légumes", "maintien",
         "quinoa, tomates, concombre, huile d'olive",
         "1. Cuire le quinoa.\n2. Couper les légumes.\n3. Mélanger.", 350),
        ("Poulet grillé healthy", "perte",
         "poulet, épices, citron",
         "1. Assaisonner.\n2. Griller 15 min.", 300),
        ("Omelette aux épinards", "maintien",
         "œufs, épinards, sel, poivre",
         "1. Battre œufs.\n2. Ajouter épinards.\n3. Cuire.", 250)
    ]
    c.executemany("INSERT INTO Recettes (nom, objectif, ingredients, instructions, calories) VALUES (?, ?, ?, ?, ?)", recettes)
    print("Recettes d'exemple insérées.")

conn.commit()
conn.close()
print("Base de données créée / vérifiée : database/users.db")
