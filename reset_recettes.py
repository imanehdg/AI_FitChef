import sqlite3

conn = sqlite3.connect("database/users.db")
c = conn.cursor()

c.execute("DELETE FROM Recettes")

conn.commit()
conn.close()

print("✅ Table Recettes vidée avec succès.")
