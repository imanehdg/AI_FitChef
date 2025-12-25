import sqlite3

conn = sqlite3.connect("database/users.db")
c = conn.cursor()

# Supprime l'ancienne table si elle existe
c.execute("DROP TABLE IF EXISTS Recettes")

# Crée la table Recettes
c.execute("""
CREATE TABLE Recettes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE,
    objectif TEXT,
    ingredients TEXT,
    instructions TEXT
)
""")

conn.commit()
conn.close()

print("Table Recettes créée avec succès.")
