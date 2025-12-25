import sqlite3

conn = sqlite3.connect("database/users.db")
c = conn.cursor()

# Supprimer ancienne table
c.execute("DROP TABLE IF EXISTS Recettes")

# Nouvelle table complète et PRO
c.execute("""
CREATE TABLE Recettes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE,
    objectif TEXT,
    type_repas TEXT,
    type_regime TEXT,
    ingredients TEXT,
    instructions TEXT,
    calories INTEGER,
    proteines INTEGER,
    glucides INTEGER,
    lipides INTEGER,
    niveau TEXT,
    image_url TEXT
)
""")

print("Nouvelle table Recettes créée ✔️")
conn.commit()
conn.close()
