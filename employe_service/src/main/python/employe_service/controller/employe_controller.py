from employe_service.service.employe_service import EmployeService

class EmployeController:
    """
    CONTRÔLEUR REST : Orchestre le flux des données pour l'API Identity.
    Fait le pont entre les routes Flask (app.py) et la logique métier (Service).
    """
    def __init__(self):
        # Initialisation de la couche service
        self.service = EmployeService()

    def afficher_annuaire(self):
        """
        MAPPING GET /api/employes
        Retourne la liste brute pour être transformée en JSON par Flask.
        """
        # On récupère les données via le service et on les renvoie immédiatement
        return self.service.lister_employe()

    def ajouter_collaborateur(self, data):
        """
        MAPPING POST /api/employes
        Extrait les données du JSON et appelle le service d'inscription.
        """
        if not data:
            return {"error": "Le corps de la requête est vide"}, 400
            
        # Appel du service avec les données extraites du dictionnaire 'data'
        nouveau_id = self.service.inscrire_employe(
            nom=data.get('nom'),
            prenom=data.get('prenom'),
            email=data.get('email'),
            role=data.get('role', 'User') # 'User' par défaut si non précisé
        )
        
        if nouveau_id:
            return {"message": "Collaborateur créé avec succès", "id": nouveau_id}, 201
        
        return {"error": "Échec de l'inscription (Vérifiez si l'email existe déjà)"}, 500

    def modifier_profil(self, id_emp, data):
        """
        MAPPING PUT /api/employes/<id>
        Met à jour les informations d'un collaborateur existant.
        """
        if not data:
            return {"error": "Données de modification manquantes"}, 400
            
        # Appel de la logique de mise à jour sécurisée
        succes = self.service.mettre_a_jour_employe(
            id_emp,
            nom=data.get('nom'),
            prenom=data.get('prenom'),
            email=data.get('email'),
            role=data.get('role'),
            password=data.get('password', 'ChangeMe123!')
        )
        
        if succes:
            return {"message": f"Le profil #{id_emp} a été mis à jour"}, 200
        
        return {"error": f"L'employé #{id_emp} est introuvable"}, 404

    def licencier_employe(self, id_emp):
        """
        MAPPING DELETE /api/employes/<id>
        Exécute la procédure de suppression physique en base.
        """
        # Le service vérifie la faisabilité technique (ex: intégrité référentielle)
        if self.service.supprimer_employe(id_emp):
            return {"message": f"L'employé #{id_emp} a été supprimé de la base"}, 200
            
        return {"error": "Action impossible (ID inexistant ou contrainte SQL)"}, 403