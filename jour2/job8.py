import mysql.connector

# Connexion sans spécifier la base pour créer "zoo" si elle n'existe pas
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Remplace par ton utilisateur MySQL
    password="root"   # Remplace par ton mot de passe MySQL
)
cursor = conn.cursor()

# Création de la base de données si elle n'existe pas
cursor.execute("CREATE DATABASE IF NOT EXISTS zoo")
cursor.close()
conn.close()

# Connexion à la base de données "zoo"
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="zoo"
)
cursor = conn.cursor()

# Création des tables
cursor.execute('''CREATE TABLE IF NOT EXISTS cage (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    superficie FLOAT NOT NULL,
                    capacite_max INT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS animal (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nom VARCHAR(255) NOT NULL,
                    race VARCHAR(255) NOT NULL,
                    cage_id INT,
                    date_naissance DATE NOT NULL,
                    pays_origine VARCHAR(255) NOT NULL,
                    FOREIGN KEY (cage_id) REFERENCES cage(id) ON DELETE SET NULL
                )''')
conn.commit()

def ajouter_cage(superficie, capacite_max):
    cursor.execute("INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)", (superficie, capacite_max))
    conn.commit()

def ajouter_animal(nom, race, cage_id, date_naissance, pays_origine):
    cursor.execute("INSERT INTO animal (nom, race, cage_id, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)",
                   (nom, race, cage_id, date_naissance, pays_origine))
    conn.commit()

def supprimer_animal(animal_id):
    cursor.execute("DELETE FROM animal WHERE id = %s", (animal_id,))
    conn.commit()

def supprimer_cage(cage_id):
    cursor.execute("UPDATE animal SET cage_id = NULL WHERE cage_id = %s", (cage_id,))  # Libérer les animaux
    cursor.execute("DELETE FROM cage WHERE id = %s", (cage_id,))
    conn.commit()

def modifier_animal(animal_id, nom, race, cage_id, date_naissance, pays_origine):
    cursor.execute("UPDATE animal SET nom = %s, race = %s, cage_id = %s, date_naissance = %s, pays_origine = %s WHERE id = %s",
                   (nom, race, cage_id, date_naissance, pays_origine, animal_id))
    conn.commit()

def afficher_animaux():
    cursor.execute("SELECT * FROM animal")
    animaux = cursor.fetchall()
    if not animaux:
        print("Aucun animal dans le zoo.")
    else:
        for row in animaux:
            print(row)

def afficher_animaux_par_cage():
    cursor.execute("SELECT c.id, c.superficie, c.capacite_max, a.id, a.nom FROM cage c LEFT JOIN animal a ON c.id = a.cage_id ORDER BY c.id")
    result = cursor.fetchall()
    cages = {}
    
    for cage_id, superficie, capacite, animal_id, animal_nom in result:
        if cage_id not in cages:
            cages[cage_id] = {"superficie": superficie, "capacite": capacite, "animaux": []}
        if animal_id:
            cages[cage_id]["animaux"].append(animal_nom)
    
    for cage_id, data in cages.items():
        animaux = data["animaux"]
        print(f"Cage {cage_id} (Superficie: {data['superficie']}m², Capacité: {data['capacite']}) : {', '.join(animaux) if animaux else 'Vide'}")

def calculer_superficie_totale():
    cursor.execute("SELECT SUM(superficie) FROM cage")
    total = cursor.fetchone()[0]
    print(f"Superficie totale des cages : {total if total else 0} m²")

# Exemple d'utilisation
ajouter_cage(50, 5)
ajouter_cage(30, 3)
ajouter_animal("Simba", "Lion", 1, "2018-05-12", "Afrique")
ajouter_animal("Zaza", "Zèbre", 1, "2019-07-14", "Afrique")
ajouter_animal("Rafiki", "Babouin", 2, "2015-03-21", "Afrique")
afficher_animaux()
afficher_animaux_par_cage()
calculer_superficie_totale()

# Fermeture de la connexion
def fermer_connexion():
    conn.close()

fermer_connexion()