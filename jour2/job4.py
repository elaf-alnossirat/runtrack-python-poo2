import mysql.connector

# pour se connecter à la database "laplateforme"
conn = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
  database = "laplateforme"
  )

# verifier la connextion 
if conn.is_connected():
   print("connecté à la database laplateforme")
else:
   print("erreur de connextion")
   
#créer un curseur pour exécuter des requetes sql
cursor = conn.cursor()

#exécuter une requete sql pour recuperer les données nom et capacites de la table "salle"
cursor.execute("SELECT nom, capacite FROM salle")

# (les resultats)
resultats = cursor.fetchall()

#afficher les resultats
print("Resultats:", resultats)

# ( une façon plus clean pour afficher les resultats):

# print("noms et capacitées de toutes les salles: ")
# for row in resultats:
#     print(f"nom: {row[0]} capacite: {row[1]}")
    
#fermer le curseur et la connection
cursor.close()
conn.close()    