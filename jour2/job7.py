import mysql.connector

#connection à mysql
conn = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
)

cursor = conn.cursor()

#creatiob d'une nouvelle base de données 
cursor.execute("CREATE DATABASE IF NOT EXISTS company")

#selection de la base de données company
cursor.execute("USE company")

#creation de la table employee (en ajoutant la clé étrangère qui pointe vers id dans service)
cursor.execute("CREATE TABLE IF NOT EXISTS employe (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255), salaire DECIMAL(10, 2), id_service INT,  FOREIGN KEY (id_service) REFERENCES service(id) ON DELETE CASCADE)")

# Insérer des données dans la table
cursor.execute("""INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Doval', 'John', 5000, 1)""")
cursor.execute("""INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Pertox', 'Jane', 6000, 2)""")
cursor.execute("""INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Obama', 'Alice', 7000, 3)""")
cursor.execute("""INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Rachal', 'Bob', 500, 4)""")
cursor.execute("""INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Tolman', 'Eve', 1400, 5)""")
cursor.execute("""INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Yori', 'Mallory', 19500, 6)""")
cursor.execute("""INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Merton', 'Charlie', 8000, 7)""")
cursor.execute("""INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Keverty', 'Victor', 7000, 8)""")
cursor.execute("""INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Domanie', 'Oscar', 9000, 9)""")
cursor.execute("""INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Gaad', 'Papa', 10000, 10)""")


# Valider les changements
conn.commit()

#une requete pour recuperer tous les employés dont le salaire est supérieur à 3 000 €.
cursor.execute("SELECT * FROM employe WHERE salaire > 3000")
resultat = cursor.fetchall()

# Afficher les employés
for employe in resultat:
    print(employe)
    
    
# ajouter la table "service"
cursor.execute("""CREATE TABLE IF NOT EXISTS service(id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255) NOT NULL)""")

# Insérer des données dans la table
services = [
    ("développeur",),
    ("développeur logiciel",),
    ("professeur",),
    ("directeur",),
    ("assistant",),
    ("alternant",),
    ("professeur",),
    ("analyste",),
    ("data analyst",),
    ("chef d'entreprise",)
]
cursor.executemany("INSERT INTO service (nom) VALUES (%s)", services)

# Valider les changements
conn.commit()

#une requete pour recuperer tous les services
cursor.execute("SELECT * FROM service")
resultat = cursor.fetchall()

# Afficher la Liste des services
print("Liste des services :") 
for service in resultat:
    print(service)
    

cursor.close()
conn.close()



