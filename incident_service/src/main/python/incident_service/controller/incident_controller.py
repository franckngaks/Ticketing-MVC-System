from incident_service.service.incident_service import IncidentService

from incident_service.service.incident_service import IncidentService

class IncidentController:
    """
    CONTRÔLEUR REST : Orchestre le flux des données pour l'API.
    Fait le pont entre les routes Flask et la logique métier du Service.
    """
    def __init__(self):
        self.service = IncidentService()

    def lister_tous_les_incidents(self):
        """Action pour le GET /api/tickets"""
        return self.service.lister_incidents()

    def creer_nouvel_incident(self, data):
        """Action pour le POST /api/tickets"""
        if not data:
            return {"error": "Corps de la requête vide"}, 400
            
        nouveau_id = self.service.ouvrir_ticket(
            titre=data.get('titre'),
            priorite=data.get('priorite'),
            id_createur=data.get('id_createur'),
            description=data.get('description')
        )
        
        if nouveau_id:
            return {"message": "Ticket créé", "id": nouveau_id}, 201
        return {"error": "Échec de création"}, 500

    def modifier_ticket_existant(self, id_ticket, data):
        """
        ACTION : UPDATE (Modification globale)
        Mapping pour la requête PUT /api/tickets/<id>
        """
        if not data:
            return {"error": "Données de modification manquantes"}, 400
            
        # On appelle le service pour appliquer les changements
        succes = self.service.modifier_ticket(
            id_ticket, 
            data.get('titre'), 
            data.get('priorite'), 
            data.get('description')
        )
        
        if succes:
            return {"message": f"Le ticket #{id_ticket} a été mis à jour"}, 200
        return {"error": "Ticket introuvable ou aucune modification effectuée"}, 404

    def resoudre_un_incident(self, id_ticket, data):
        """Action pour le PUT /api/tickets/<id>/resolve"""
        id_tech = data.get('id_technicien')
        if not id_tech:
            return {"error": "ID Technicien requis"}, 400

        resultat = self.service.cloturer_incident(id_ticket, id_tech)
        
        if resultat:
            return {"message": f"Ticket #{id_ticket} résolu"}, 200
        return {"error": "Action refusée (droits ou existence)"}, 403