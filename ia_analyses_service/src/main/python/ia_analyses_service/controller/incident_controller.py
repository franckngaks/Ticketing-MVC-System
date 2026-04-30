# ia_analyses_service/service/incident_controller.py

class IncidentController:
    def __init__(self, manager):
        self.manager = manager

    def lancer_analyse_globale(self):
        """Orchestre le traitement de tous les nouveaux incidents."""
        try:
            # On appelle la logique métier que tu as déjà codée
            resultats = self.manager.executer_analyse_complete()
            return {"status": "success", "message": "Analyse terminée avec succès"}
        except Exception as e:
            return {"status": "error", "message": str(e)}