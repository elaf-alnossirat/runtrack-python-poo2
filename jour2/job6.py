import mysql.connector


conn = mysql.connector.connect(
    host="localhost",        
    user="root",       
    password="root",  
    database="laplateforme" 
)


if conn.is_connected():
    print("connecté à la database laplateforme")
else:
    print("Erreur de connexion")


cursor = conn.cursor()

# Exécuter la requête pour calculer la capacitée de toutes les salles 
cursor.execute("SELECT SUM(capacite) FROM salle")


resultat = cursor.fetchone()

# Afficher la superficie totale
print(f"La capacitée de toutes les salles est de {resultat[0]} personnes")


cursor.close()
conn.close()