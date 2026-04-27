from service.incidentService import IncidentService

class IncidentController:
    """
    CONTRÔLEUR : GÈRE LE FLUX DES INCIDENTS (TICKETING).
    FAIT LE PONT ENTRE L'INTERFACE (MAIN) ET LA LOGIQUE MÉTIER (SERVICE).
    """
    def __init__(self):
        self.service = IncidentService()

    def afficher_liste_incidents(self):
        """ACTION : READ - RÉCUPÈRE ET AFFICHE TOUS LES TICKETS."""
        print("\n📋 --- REGISTRE DES INCIDENTS ---")
        incidents = self.service.lister_incidents()
        
        if not incidents:
            print("Aucun ticket en cours en base de données.")
        else:
            for i in incidents:
                print(f"#{i['id']} | [{i['priorite']}] | {i['statut']} | {i['titre']} (Auteur: {i['prenom']} {i['nom']})")

    def ouvrir_ticket(self, titre, priorite, id_createur, description):
        """ACTION : CREATE - CRÉE UN NOUVEL INCIDENT VIA LE SERVICE."""
        print(f"\n🚀 Ouverture du ticket : '{titre}'...")
        nouveau_id = self.service.ouvrir_ticket(titre, priorite, id_createur, description)
        
        if nouveau_id:
            print(f"✅ SUCCÈS : Ticket #{nouveau_id} enregistré (ID généré par la BD).")
            return nouveau_id
        else:
            print("❌ ÉCHEC : Impossible de créer le ticket. Vérifiez l'ID du créateur.")
            return None

    def modifier_ticket(self, id_ticket, titre, priorite, description):
        """ACTION : UPDATE INFO - MODIFIE LES TEXTES ET LA PRIORITÉ D'UN TICKET."""
        print(f"\n📝 Mise à jour des informations du ticket #{id_ticket}...")
        if self.service.modifier_ticket(id_ticket, titre, priorite, description):
            print(f"✅ SUCCÈS : Les informations du ticket #{id_ticket} ont été mises à jour.")
        else:
            print(f"❌ ÉCHEC : Modification impossible (Le ticket #{id_ticket} existe-t-il ?).")

    def resoudre_ticket(self, id_ticket, id_technicien):
        """ACTION : UPDATE STATUS - CLÔTURE UN TICKET PAR UN TECHNICIEN."""
        print(f"\n🛠️ Résolution du ticket #{id_ticket} par le technicien #{id_technicien}...")
        if self.service.cloturer_incident(id_ticket, id_technicien):
            print(f"✅ SUCCÈS : Le ticket #{id_ticket} est désormais 'Résolu'.")
        else:
            print(f"❌ ÉCHEC : Résolution refusée (Vérifiez les IDs ou les droits du tech).")