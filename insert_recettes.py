import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("database/users.db")
c = conn.cursor()

# ÉTAPE 1 : Ajouter les nouvelles colonnes si elles n'existent pas
print("🔧 Vérification de la structure de la table...")
try:
    c.execute("ALTER TABLE Recettes ADD COLUMN temps INTEGER")
    print("✅ Colonne 'temps' ajoutée")
except:
    print("⚠️  Colonne 'temps' existe déjà")

try:
    c.execute("ALTER TABLE Recettes ADD COLUMN calories INTEGER")
    print("✅ Colonne 'calories' ajoutée")
except:
    print("⚠️  Colonne 'calories' existe déjà")

try:
    c.execute("ALTER TABLE Recettes ADD COLUMN photo TEXT")
    print("✅ Colonne 'photo' ajoutée")
except:
    print("⚠️  Colonne 'photo' existe déjà")

conn.commit()

# ÉTAPE 2 : Liste complète de recettes avec TOUTES les infos
recettes = [
    # ========================================
    # RECETTES POUR PERTE DE POIDS (low calorie)
    # ========================================
    {
        "nom": "Salade Poulet Quinoa",
        "objectif": "perte",
        "ingredients": "quinoa, poulet, tomates, concombre, citron, huile d'olive",
        "instructions": "1. Cuire le quinoa pendant 15 min\n2. Griller le poulet\n3. Couper les légumes\n4. Mélanger le tout avec du citron",
        "temps": 20,
        "calories": 350,
        "photo": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400"
    },
    {
        "nom": "Soupe Légumes Detox",
        "objectif": "perte",
        "ingredients": "courgettes, carottes, céleri, oignon, bouillon, ail",
        "instructions": "1. Faire revenir l'oignon et l'ail\n2. Ajouter les légumes coupés\n3. Couvrir de bouillon\n4. Laisser mijoter 20 min",
        "temps": 25,
        "calories": 180,
        "photo": "https://images.unsplash.com/photo-1547592166-23ac45744acd?w=400"
    },
    {
        "nom": "Bowl Saumon Avocat",
        "objectif": "perte",
        "ingredients": "saumon, avocat, riz complet, edamame, concombre, sauce soja",
        "instructions": "1. Cuire le riz complet\n2. Griller le saumon\n3. Couper l'avocat et le concombre\n4. Assembler dans un bol",
        "temps": 25,
        "calories": 420,
        "photo": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400"
    },
    {
        "nom": "Salade Grecque Light",
        "objectif": "perte",
        "ingredients": "tomates, concombre, feta, olives, oignon rouge, huile d'olive",
        "instructions": "1. Couper tous les légumes en dés\n2. Ajouter la feta émiettée\n3. Assaisonner avec huile d'olive et citron",
        "temps": 10,
        "calories": 280,
        "photo": "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=400"
    },
    {
        "nom": "Wok Légumes Crevettes",
        "objectif": "perte",
        "ingredients": "crevettes, brocoli, poivrons, carottes, sauce soja, gingembre",
        "instructions": "1. Faire sauter les crevettes\n2. Ajouter les légumes\n3. Assaisonner avec sauce soja et gingembre\n4. Cuire 10 min",
        "temps": 15,
        "calories": 320,
        "photo": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400"
    },
    {
        "nom": "Omelette Légumes",
        "objectif": "perte",
        "ingredients": "oeufs, tomates, épinards, champignons, oignon",
        "instructions": "1. Battre 3 oeufs\n2. Faire revenir les légumes\n3. Verser les oeufs\n4. Cuire 5 min",
        "temps": 12,
        "calories": 250,
        "photo": "https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400"
    },
    {
        "nom": "Poulet Rôti Légumes",
        "objectif": "perte",
        "ingredients": "poulet, brocoli, carottes, courgettes, huile d'olive, herbes",
        "instructions": "1. Couper les légumes\n2. Assaisonner le poulet\n3. Enfourner 30 min à 200°C",
        "temps": 35,
        "calories": 380,
        "photo": "https://images.unsplash.com/photo-1598103442097-8b74394b95c6?w=400"
    },
    {
        "nom": "Smoothie Bowl Fruits Rouges",
        "objectif": "perte",
        "ingredients": "fraises, myrtilles, banane, yaourt grec, granola",
        "instructions": "1. Mixer les fruits avec le yaourt\n2. Verser dans un bol\n3. Ajouter le granola",
        "temps": 8,
        "calories": 290,
        "photo": "https://images.unsplash.com/photo-1590301157890-4810ed352733?w=400"
    },
    {
        "nom": "Salade Thon Haricots",
        "objectif": "perte",
        "ingredients": "thon, haricots verts, tomates, oeufs, olives, vinaigre",
        "instructions": "1. Cuire les haricots et les oeufs\n2. Mélanger avec le thon\n3. Assaisonner",
        "temps": 18,
        "calories": 310,
        "photo": "https://images.unsplash.com/photo-1551248429-40975aa4de74?w=400"
    },
    {
        "nom": "Courgettes Farcies",
        "objectif": "perte",
        "ingredients": "courgettes, viande hachée, tomates, oignon, ail, herbes",
        "instructions": "1. Évider les courgettes\n2. Préparer la farce\n3. Farcir et enfourner 25 min",
        "temps": 30,
        "calories": 270,
        "photo": "https://images.unsplash.com/photo-1604908815679-47f85a1d4edb?w=400"
    },
    
    # ========================================
    # RECETTES POUR PRISE DE MUSCLE (high protein)
    # ========================================
    {
        "nom": "Bowl Poulet Riz Brocoli",
        "objectif": "gain",
        "ingredients": "poulet, riz basmati, brocoli, sauce teriyaki",
        "instructions": "1. Cuire le riz\n2. Griller le poulet\n3. Cuire le brocoli à la vapeur\n4. Assembler avec la sauce",
        "temps": 25,
        "calories": 550,
        "photo": "https://images.unsplash.com/photo-1546069901-eacef0df6022?w=400"
    },
    {
        "nom": "Omelette Protéinée",
        "objectif": "gain",
        "ingredients": "oeufs, fromage, jambon, tomates, champignons",
        "instructions": "1. Battre 4 oeufs\n2. Ajouter le jambon et fromage\n3. Cuire avec les légumes\n4. Plier en deux",
        "temps": 10,
        "calories": 480,
        "photo": "https://images.unsplash.com/photo-1612240498262-8e1e3c2c0b4d?w=400"
    },
    {
        "nom": "Pâtes Saumon Épinards",
        "objectif": "gain",
        "ingredients": "pâtes complètes, saumon, épinards, crème, ail",
        "instructions": "1. Cuire les pâtes\n2. Faire revenir le saumon\n3. Ajouter épinards et crème\n4. Mélanger",
        "temps": 20,
        "calories": 620,
        "photo": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=400"
    },
    {
        "nom": "Steak Patates Douces",
        "objectif": "gain",
        "ingredients": "steak, patates douces, brocoli, beurre, ail",
        "instructions": "1. Cuire les patates au four\n2. Griller le steak\n3. Cuire le brocoli\n4. Servir ensemble",
        "temps": 35,
        "calories": 680,
        "photo": "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=400"
    },
    {
        "nom": "Wrap Poulet Avocat",
        "objectif": "gain",
        "ingredients": "tortilla, poulet, avocat, tomates, fromage, sauce",
        "instructions": "1. Griller le poulet\n2. Couper l'avocat\n3. Garnir la tortilla\n4. Rouler et couper",
        "temps": 15,
        "calories": 520,
        "photo": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=400"
    },
    {
        "nom": "Riz Sauté Crevettes",
        "objectif": "gain",
        "ingredients": "riz, crevettes, oeufs, petits pois, carottes, sauce soja",
        "instructions": "1. Cuire le riz\n2. Faire sauter les crevettes\n3. Ajouter légumes et riz\n4. Mélanger avec sauce",
        "temps": 22,
        "calories": 580,
        "photo": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400"
    },
    {
        "nom": "Burger Protéiné Maison",
        "objectif": "gain",
        "ingredients": "pain complet, steak haché, fromage, tomate, salade, oignon",
        "instructions": "1. Griller le steak\n2. Toaster le pain\n3. Assembler le burger\n4. Ajouter les légumes",
        "temps": 18,
        "calories": 650,
        "photo": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400"
    },
    {
        "nom": "Quinoa Bowl Thon",
        "objectif": "gain",
        "ingredients": "quinoa, thon, avocat, tomates, maïs, citron",
        "instructions": "1. Cuire le quinoa\n2. Émietter le thon\n3. Couper les légumes\n4. Mélanger le tout",
        "temps": 20,
        "calories": 540,
        "photo": "https://images.unsplash.com/photo-1623428187425-5f4e39b93d42?w=400"
    },
    {
        "nom": "Pancakes Protéinés",
        "objectif": "gain",
        "ingredients": "oeufs, farine, lait, poudre protéine, banane",
        "instructions": "1. Mélanger tous les ingrédients\n2. Faire cuire dans une poêle\n3. Servir avec fruits",
        "temps": 15,
        "calories": 450,
        "photo": "https://images.unsplash.com/photo-1528207776546-365bb710ee93?w=400"
    },
    {
        "nom": "Pâtes Bolognaise Complètes",
        "objectif": "gain",
        "ingredients": "pâtes complètes, viande hachée, tomates, oignon, ail, basilic",
        "instructions": "1. Cuire les pâtes\n2. Préparer la sauce bolognaise\n3. Laisser mijoter 20 min\n4. Mélanger",
        "temps": 30,
        "calories": 620,
        "photo": "https://images.unsplash.com/photo-1598866594230-a7c12756260f?w=400"
    },
    
    # ========================================
    # RECETTES POUR MAINTIEN (équilibré)
    # ========================================
    {
        "nom": "Bowl Buddha Équilibré",
        "objectif": "maintien",
        "ingredients": "riz, pois chiches, avocat, carottes, chou rouge, tahini",
        "instructions": "1. Cuire le riz et les pois chiches\n2. Préparer les légumes\n3. Assembler dans un bol\n4. Ajouter la sauce tahini",
        "temps": 28,
        "calories": 480,
        "photo": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400"
    },
    {
        "nom": "Poulet Curry Légumes",
        "objectif": "maintien",
        "ingredients": "poulet, lait coco, curry, courgettes, poivrons, oignon",
        "instructions": "1. Faire revenir le poulet\n2. Ajouter légumes et curry\n3. Verser le lait de coco\n4. Mijoter 15 min",
        "temps": 30,
        "calories": 420,
        "photo": "https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?w=400"
    },
    {
        "nom": "Tacos Végétariens",
        "objectif": "maintien",
        "ingredients": "tortillas, haricots noirs, maïs, tomates, avocat, fromage",
        "instructions": "1. Chauffer les tortillas\n2. Préparer les haricots\n3. Garnir avec les légumes\n4. Ajouter fromage et avocat",
        "temps": 20,
        "calories": 450,
        "photo": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=400"
    },
    {
        "nom": "Saumon Teriyaki Riz",
        "objectif": "maintien",
        "ingredients": "saumon, riz, sauce teriyaki, brocoli, sésame",
        "instructions": "1. Mariner le saumon\n2. Cuire le riz\n3. Griller le saumon\n4. Servir avec brocoli",
        "temps": 25,
        "calories": 510,
        "photo": "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=400"
    },
    {
        "nom": "Pizza Végétarienne Maison",
        "objectif": "maintien",
        "ingredients": "pâte, sauce tomate, mozzarella, poivrons, champignons, olives",
        "instructions": "1. Étaler la pâte\n2. Ajouter sauce et fromage\n3. Garnir de légumes\n4. Enfourner 15 min",
        "temps": 25,
        "calories": 490,
        "photo": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400"
    },
    {
        "nom": "Wok Nouilles Légumes",
        "objectif": "maintien",
        "ingredients": "nouilles, brocoli, carottes, poivrons, sauce soja, gingembre",
        "instructions": "1. Cuire les nouilles\n2. Faire sauter les légumes\n3. Ajouter sauce et gingembre\n4. Mélanger avec nouilles",
        "temps": 18,
        "calories": 410,
        "photo": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=400"
    },
    {
        "nom": "Salade Quinoa Feta",
        "objectif": "maintien",
        "ingredients": "quinoa, feta, tomates, concombre, olives, menthe",
        "instructions": "1. Cuire le quinoa\n2. Couper les légumes\n3. Émietter la feta\n4. Mélanger avec menthe",
        "temps": 20,
        "calories": 390,
        "photo": "https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?w=400"
    },
    {
        "nom": "Risotto Champignons",
        "objectif": "maintien",
        "ingredients": "riz arborio, champignons, bouillon, parmesan, vin blanc",
        "instructions": "1. Faire revenir les champignons\n2. Ajouter le riz\n3. Verser le bouillon progressivement\n4. Ajouter le parmesan",
        "temps": 35,
        "calories": 470,
        "photo": "https://images.unsplash.com/photo-1476124369491-f381bc6e7d76?w=400"
    },
    {
        "nom": "Chili Con Carne",
        "objectif": "maintien",
        "ingredients": "viande hachée, haricots rouges, tomates, oignon, épices",
        "instructions": "1. Faire revenir la viande\n2. Ajouter oignon et épices\n3. Ajouter tomates et haricots\n4. Mijoter 30 min",
        "temps": 40,
        "calories": 520,
        "photo": "https://images.unsplash.com/photo-1603532497295-0c0add57ed13?w=400"
    },
    {
        "nom": "Tartine Avocat Oeuf",
        "objectif": "maintien",
        "ingredients": "pain complet, avocat, oeuf, tomates cerises, feta",
        "instructions": "1. Toaster le pain\n2. Écraser l'avocat\n3. Pocher l'oeuf\n4. Assembler et garnir",
        "temps": 12,
        "calories": 380,
        "photo": "https://images.unsplash.com/photo-1525351484163-7529414344d8?w=400"
    }
]

# ÉTAPE 3 : Insérer toutes les recettes
print("\n🔄 Ajout des recettes dans la base de données...")
count_added = 0
count_exists = 0

for recette in recettes:
    try:
        c.execute("""
            INSERT INTO Recettes (nom, objectif, ingredients, instructions, temps, calories, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            recette["nom"], 
            recette["objectif"], 
            recette["ingredients"], 
            recette["instructions"],
            recette["temps"],
            recette["calories"],
            recette["photo"]
        ))
        print(f"✅ {recette['nom']} ({recette['temps']}min, {recette['calories']}kcal)")
        count_added += 1
    except sqlite3.IntegrityError:
        print(f"⚠️  Existe déjà : {recette['nom']}")
        count_exists += 1

conn.commit()
conn.close()

print(f"\n🎉 TERMINÉ !")
print(f"📊 Ajoutées : {count_added} recettes")
print(f"⚠️  Existantes : {count_exists} recettes")
print(f"💾 Total : {len(recettes)} recettes")
print("   - Perte : 10 recettes")
print("   - Gain : 10 recettes")
print("   - Maintien : 10 recettes")