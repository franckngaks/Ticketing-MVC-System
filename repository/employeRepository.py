from config.databaseConnexion import get_connection

class EmployeRepository:
    """
    COUCHE ACCÈS AUX DONNÉES : Exécute le SQL brut.
    """

    def find_all(self):
        conn = get_connection()
        if not conn: return []
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM employes ORDER BY id ASC")
            return cursor.fetchall()
        finally:
            conn.close()

    def find_by_id(self, id_emp):
        conn = get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id FROM employes WHERE id = %s", (id_emp,))
            return cursor.fetchone()
        finally:
            conn.close()

    def save(self, nom, prenom, email, password, role):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO employes (nom, prenom, email, password_hash, role) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (nom, prenom, email, password, role))
            conn.commit()
            return cursor.lastrowid
        finally:
            conn.close()

    def update(self, id_emp, nom, prenom, email, password, role):
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
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employes WHERE id = %s", (id_emp,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()