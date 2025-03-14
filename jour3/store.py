import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox

# Connexion au serveur MySQL (création de la base de données si elle n'existe pas)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS store")
cursor.close()
conn.close()

# Connexion à la base de données 'store'
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="store"
)
cursor = conn.cursor()

# Création des tables si elles n'existent pas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS category (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        price INT NOT NULL,
        quantity INT NOT NULL,
        id_category INT,
        FOREIGN KEY (id_category) REFERENCES category(id) ON DELETE CASCADE
    )
''')
conn.commit()

# Fonction pour actualiser la liste des catégories
def update_category_list():
    cursor.execute("SELECT name FROM category")
    categories = [row[0] for row in cursor.fetchall()]
    category_combobox['values'] = categories
    return categories

# Fonction pour ajouter une catégorie
def add_category():
    category_name = category_entry.get()
    if category_name:
        cursor.execute("INSERT INTO category (name) VALUES (%s)", (category_name,))
        conn.commit()
        messagebox.showinfo("Succès", "Catégorie ajoutée avec succès")
        update_category_list()
        category_entry.delete(0, END)
    else:
        messagebox.showwarning("Attention", "Veuillez entrer un nom de catégorie")

# Fonction pour ajouter un produit
def add_product():
    name = name_entry.get()
    desc = desc_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    category = category_combobox.get()
    
    if not (name and price and quantity and category):
        messagebox.showwarning("Attention", "Veuillez remplir tous les champs")
        return
    
    cursor.execute("SELECT id FROM category WHERE name = %s", (category,))
    category_id = cursor.fetchone()
    if category_id:
        cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
                       (name, desc, price, quantity, category_id[0]))
        conn.commit()
        messagebox.showinfo("Succès", "Produit ajouté avec succès")
        refresh_table()
    else:
        messagebox.showerror("Erreur", "Catégorie introuvable")

# Fonction pour supprimer un produit
def delete_product():
    selected_item = tree.selection()
    if selected_item:
        product_id = tree.item(selected_item)['values'][0]
        cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
        conn.commit()
        refresh_table()
    else:
        messagebox.showwarning("Attention", "Veuillez sélectionner un produit")

# Fonction pour actualiser l'affichage
def refresh_table():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT product.id, product.name, category.name, product.price, product.quantity FROM product JOIN category ON product.id_category = category.id")
    for row in cursor.fetchall():
        tree.insert('', END, values=row)

# Interface graphique améliorée
root = Tk()
root.title("Gestion de Stock")
root.configure(bg="#f4f4f4")

frame = Frame(root, bg="#f4f4f4", padx=20, pady=20)
frame.pack()

Label(frame, text="Nom Produit", bg="#f4f4f4").grid(row=0, column=0, padx=10, pady=5)
name_entry = Entry(frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

Label(frame, text="Description", bg="#f4f4f4").grid(row=1, column=0, padx=10, pady=5)
desc_entry = Entry(frame, width=30)
desc_entry.grid(row=1, column=1, padx=10, pady=5)

Label(frame, text="Prix", bg="#f4f4f4").grid(row=2, column=0, padx=10, pady=5)
price_entry = Entry(frame, width=30)
price_entry.grid(row=2, column=1, padx=10, pady=5)

Label(frame, text="Quantité", bg="#f4f4f4").grid(row=3, column=0, padx=10, pady=5)
quantity_entry = Entry(frame, width=30)
quantity_entry.grid(row=3, column=1, padx=10, pady=5)

Label(frame, text="Catégorie", bg="#f4f4f4").grid(row=4, column=0, padx=10, pady=5)
category_combobox = ttk.Combobox(frame, width=27)
category_combobox.grid(row=4, column=1, padx=10, pady=5)
update_category_list()

Button(frame, text="Ajouter Produit", command=add_product, bg="#4CAF50", fg="white", width=15).grid(row=5, column=0, padx=10, pady=5)
Button(frame, text="Supprimer Produit", command=delete_product, bg="#FF5733", fg="white", width=15).grid(row=5, column=1, padx=10, pady=5)

Label(frame, text="Nouvelle Catégorie", bg="#f4f4f4").grid(row=6, column=0, padx=10, pady=5)
category_entry = Entry(frame, width=30)
category_entry.grid(row=6, column=1, padx=10, pady=5)

Button(frame, text="Ajouter Catégorie", command=add_category, bg="#2196F3", fg="white", width=15).grid(row=7, column=1, padx=10, pady=5)

# Tableau des produits
tree = ttk.Treeview(root, columns=("ID", "Nom", "Catégorie", "Prix", "Quantité"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Nom", text="Nom")
tree.heading("Catégorie", text="Catégorie")
tree.heading("Prix", text="Prix")
tree.heading("Quantité", text="Quantité")
tree.pack(pady=10)

refresh_table()

# Fermeture de la connexion proprement
def close_connection():
    cursor.close()
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_connection)
root.mainloop()
 