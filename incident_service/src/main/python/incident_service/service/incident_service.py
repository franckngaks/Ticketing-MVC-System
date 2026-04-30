from incident_service.repository.incident_repository import IncidentRepository

class IncidentService:
    """
    COUCHE SERVICE : L'intelligence métier de l'application.
    Fait le lien entre le contrôleur et le repository en appliquant les règles de gestion.
    """

    def __init__(self):
        # Injection du repository pour l'accès aux données
        self.repository = IncidentRepository()

    def lister_incidents(self):
        """
        Action : READ (Logique métier)
        Récupère tous les incidents enrichis des noms des auteurs via le repository.
        """
        return self.repository.find_all()

    def ouvrir_ticket(self, titre, priorite, id_createur, description):
        """
        Action : CREATE (Logique métier)
        Valide que les informations essentielles sont présentes.
        """
        if not titre.strip() or not description.strip():
            print("⚠️ Erreur métier : Le titre et la description sont obligatoires.")
            return False

        return self.repository.save(titre, priorite, id_createur, description)

    def modifier_ticket(self, id_ticket, titre, priorite, description):
        """
        Action : UPDATE (Logique métier)
        Vérifie la validité des nouvelles informations avant modification.
        """
        # RÈGLE MÉTIER : On ne peut pas vider un titre ou une description lors d'une modification
        if not titre.strip() or not description.strip():
            print("⚠️ Erreur métier : Les nouveaux champs ne peuvent pas être vides.")
            return False
            
        # Appel au repository pour la mise à jour SQL
        return self.repository.modifier_ticket(id_ticket, titre, priorite, description)

    def cloturer_incident(self, id_ticket, id_technicien):
        """
        Action : UPDATE (Logique métier de résolution)
        RÈGLE MÉTIER : Seul un profil 'Tech' ou 'Admin' peut résoudre un incident.
        """
        role = self.repository.get_user_role(id_technicien)

        if role not in ['Tech', 'Admin']:
            print(f"⚠️ Blocage métier : L'utilisateur #{id_technicien} ({role}) n'a pas les droits pour résoudre un ticket.")
            return False

        return self.repository.update_status_to_resolved(id_ticket, id_technicien)

    def suggerer_priorite(self, titre):
        """Aide au diagnostic automatique."""
        mots_urgents = ["bloqué", "panne", "serveur", "crash", "incendie"]
        if any(mot in titre.lower() for mot in mots_urgents):
            return "Critique"
        return "Moyenne"