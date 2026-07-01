from ticket_service.config.database import get_connection

class IncidentRepository:
    """
    COUCHE REPOSITORY : Gère uniquement les accès à la base de données (SQL).
    """

    def find_all(self):
        """Récupère tous les incidents avec jointure sur l'auteur."""
        conn = get_connection()
        if conn is None: return []
        try:
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT i.*, e.nom, e.prenom FROM incidents i JOIN employes e ON i.id_createur = e.id ORDER BY i.date_creation DESC"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            conn.close()

    def save(self, titre, priorite, id_createur, description):
        """Insère un nouvel incident."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO incidents (titre, priorite, id_createur, description, statut) VALUES (%s, %s, %s, %s, 'Ouvert')"
            cursor.execute(sql, (titre, priorite, id_createur, description))
            conn.commit()
            return cursor.lastrowid
        finally:
            conn.close()

    def modifier_ticket(self, id_ticket, titre, priorite, description):
        """
        ACTION REQUISE : Met à jour les informations textuelles d'un ticket.
        C'est cette méthode qui manquait et provoquait votre erreur.
        """
        conn = get_connection()
        if conn is None: return False
        try:
            cursor = conn.cursor()
            sql = "UPDATE incidents SET titre = %s, priorite = %s, description = %s WHERE id = %s"
            cursor.execute(sql, (titre, priorite, description, id_ticket))
            conn.commit()
            return True
        except Exception as e:
            print(f"❌ Erreur SQL (Update) : {e}")
            return False
        finally:
            conn.close()

    def update_status_to_resolved(self, id_ticket, id_technicien):
        """Marque un ticket comme résolu."""
        conn = get_connection()
        try:
            cursor = conn.cursor()
            sql = "UPDATE incidents SET statut = 'Résolu', id_technicien = %s WHERE id = %s"
            cursor.execute(sql, (id_technicien, id_ticket))
            conn.commit()
            return True
        finally:
            conn.close()

    def get_user_role(self, user_id):
        """Récupère le rôle d'un employé."""
        conn = get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT role FROM employes WHERE id = %s", (user_id,))
            res = cursor.fetchone()
            return res['role'] if res else None
        finally:
            conn.close()