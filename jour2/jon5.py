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

# Exécuter la requête pour calculer la superficie totale de tous les étages
cursor.execute("SELECT SUM(superficie) FROM etage")


resultat = cursor.fetchone()

# Afficher la superficie totale
print(f"La superficie de La Plateforme est de {resultat[0]} m²")


cursor.close()
conn.close()
