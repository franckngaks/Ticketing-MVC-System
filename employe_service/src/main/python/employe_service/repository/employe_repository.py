from employe_service.config.database import get_connection

class EmployeRepository:
    """
    COUCHE ACCÈS AUX DONNÉES (Data Access Layer - DAL) :
    Cette classe est l'unique interface entre l'application Python et la base de données MySQL.
    
    Son rôle est purement technique : elle exécute les requêtes SQL brutes sans se soucier 
    de la logique métier (qui est gérée par le Service).
    """

    def find_all(self):
        """
        Action : READ (Lecture Globale)
        Récupère l'intégralité de l'annuaire des employés.
        
        Returns:
            list[dict]: Une liste de dictionnaires représentant les lignes de la table.
        """
        conn = get_connection()
        if not conn: return []
        try:
            # dictionary=True transforme les tuples SQL en dictionnaires Python {colonne: valeur}
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM employes ORDER BY id ASC")
            return cursor.fetchall()
        finally:
            # Libération systématique de la connexion pour éviter la saturation du serveur
            conn.close()

    def find_by_id(self, id_emp):
        """
        Action : READ (Lecture Ciblée)
        Vérifie l'existence d'un employé spécifique via son identifiant unique.
        
        Args:
            id_emp (int): L'ID de l'employé à rechercher.
            
        Returns:
            dict | None: Les données de l'employé ou None s'il n'existe pas.
        """
        conn = get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            # Utilisation de %s pour prévenir les injections SQL
            cursor.execute("SELECT id FROM employes WHERE id = %s", (id_emp,))
            return cursor.fetchone()
        finally:
            conn.close()

    def save(self, nom, prenom, email, password, role):
        """
        Action : CREATE (Insertion)
        Enregistre un nouveau collaborateur physiquement sur le disque dur.
        
        Returns:
            int: L'ID auto-généré par la base de données (AUTO_INCREMENT).
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO employes (nom, prenom, email, password_hash, role) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (nom, prenom, email, password, role))
            
            # Validation de la transaction pour rendre l'écriture permanente
            conn.commit()
            return cursor.lastrowid
        finally:
            conn.close()

    def update(self, id_emp, nom, prenom, email, password, role):
        """
        Action : UPDATE (Modification)
        Met à jour l'ensemble des informations d'un profil existant.
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = """
                UPDATE employes 
                SET nom = %s, prenom = %s, email = %s, password_hash = %s, role = %s 
                WHERE id = %s
            """
            cursor.execute(sql, (nom, prenom, email, password, role, id_emp))
            conn.commit()
            return True
        finally:
            conn.close()

    def delete(self, id_emp):
        """
        Action : DELETE (Suppression)
        Retire définitivement un employé de l'organisation.
        
        Returns:
            bool: True si au moins une ligne a été supprimée, False sinon.
        """
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employes WHERE id = %s", (id_emp,))
            conn.commit()
            # rowcount permet de vérifier si l'ID existait vraiment au moment de la suppression
            return cursor.rowcount > 0
        finally:
            conn.close()