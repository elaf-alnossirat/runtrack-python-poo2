CREATE TABLE etage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    numero INT,
    superficie INT
);

CREATE TABLE salle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    id_etage INT,
    capacite INT,
    FOREIGN KEY (id_etage) REFERENCES etage(id)
);



mysql> SHOW TABLES;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etage                  |
| etudiant               |
| salle                  |
+------------------------+
3 rows in set (0.00 sec)

mysql> DESCRIBE salle;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| nom      | varchar(255) | YES  |     | NULL    |                |
| id_etage | int          | YES  | MUL | NULL    |                |
| capacite | int          | YES  |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql> DESCRIBE etage;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| nom        | varchar(255) | YES  |     | NULL    |
   |
| numero     | int          | YES  |     | NULL    |
   |
| superficie | int          | YES  |     | NULL    |
   |
+------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)