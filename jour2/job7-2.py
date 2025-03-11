#============================================================#

# une classe Python Employe qui permet d'effectuer les opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) sur la table employe.


import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        """Initialise la connexion à la base de données"""
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.creer_table()

    def creer_table(self):
        """Crée la table employe si elle n'existe pas"""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employe (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255) NOT NULL,
            prenom VARCHAR(255) NOT NULL,
            salaire DECIMAL(10, 2) NOT NULL,
            id_service INT NOT NULL
        )
        """)
        self.conn.commit()

    def ajouter_employe(self, nom, prenom, salaire, id_service):
        """Ajoute un employé dans la base de données"""
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        valeurs = (nom, prenom, salaire, id_service)
        self.cursor.execute(sql, valeurs)
        self.conn.commit()
        print("✅ Employé ajouté avec succès.")

    def afficher_employes(self):
        """Affiche tous les employés"""
        self.cursor.execute("SELECT * FROM employe")
        employes = self.cursor.fetchall()
        for employe in employes:
            print(employe)

    def mettre_a_jour_salaire(self, employe_id, nouveau_salaire):
        """Met à jour le salaire d'un employé"""
        sql = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.cursor.execute(sql, (nouveau_salaire, employe_id))
        self.conn.commit()
        print("✅ Salaire mis à jour.")

    def supprimer_employe(self, employe_id):
        """Supprime un employé de la base de données"""
        sql = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(sql, (employe_id,))
        self.conn.commit()
        print("✅ Employé supprimé.")

    def fermer_connexion(self):
        """Ferme la connexion à la base de données"""
        self.cursor.close()
        self.conn.close()
        print("🔒 Connexion fermée.")

# ================== TEST DE LA CLASSE ==================
if __name__ == "__main__":
    db = Employe(host="localhost", user="root", password="root", database="company")

    # Ajouter des employés
    db.ajouter_employe("Dupont", "Jean", 3500.00, 1)
    db.ajouter_employe("Martin", "Alice", 4200.00, 2)

    # Afficher tous les employés
    print("\n📋 Liste des employés :")
    db.afficher_employes()

    # Mettre à jour un salaire
    db.mettre_a_jour_salaire(1, 4000.00)

    # Supprimer un employé
    db.supprimer_employe(2)

    # Vérifier les employés après modifications
    print("\n📋 Liste des employés après modifications :")
    db.afficher_employes()

    # Fermer la connexion
    db.fermer_connexion()
