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

#exécuter une requete sql pour recuperer les données de la table "etudiant"
cursor.execute("SELECT * FROM etudiant")

#récupérer les données de la table "etudiant" (les resultats)
resultats = cursor.fetchall()

#afficher les resultats
for row in resultats:
    print(row) 
    
#fermer le curseur et la connection
cursor.close()
conn.close()    