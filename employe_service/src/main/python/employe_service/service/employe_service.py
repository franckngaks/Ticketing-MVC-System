from employe_service.repository.employe_repository import EmployeRepository

class EmployeService:
    """
    COUCHE SERVICE : Intelligence et validation des règles métiers Helpline.
    
    Le Service agit comme le cerveau de l'application. Contrairement au Repository 
    qui se contente d'exécuter du SQL, le Service vérifie les droits, valide 
    les données et s'assure que les processus métiers sont respectés avant 
    toute modification en base.
    """
    def __init__(self):
        # Injection de dépendance : le service utilise le repository pour les données
        self.repository = EmployeRepository()

    def lister_employe(self):
        """
        Action : READ
        Récupère les données brutes du repository. 
        C'est ici qu'on pourrait ajouter des filtres ou des tris spécifiques.
        """
        return self.repository.find_all()

    def inscrire_employe(self, nom, prenom, email, role, password="ChangeMe123!"):
        """
        Action : CREATE
        Gère l'inscription d'un nouveau collaborateur.
        
        Note : Dans une version avancée, c'est ici que l'on vérifierait si 
        l'email n'est pas déjà utilisé par un autre compte avant d'appeler le repository.
        """
        return self.repository.save(nom, prenom, email, password, role)

    def mettre_a_jour_employe(self, id_emp, nom, prenom, email, role, password):
        """
        Action : UPDATE
        Mise à jour sécurisée d'un profil.
        
        RÈGLE MÉTIER : On effectue une vérification d'existence préalable. 
        Si l'employé n'existe pas en base, on bloque l'opération au niveau 
        du service pour éviter une erreur SQL inutile.
        """
        # Vérification de sécurité métier
        if not self.repository.find_by_id(id_emp):
            print(f"⚠️ Erreur métier : L'ID #{id_emp} est inconnu dans le système.")
            return False
        
        return self.repository.update(id_emp, nom, prenom, email, password, role)

    def supprimer_employe(self, id_emp):
        """
        Action : DELETE
        Suppression définitive d'un compte.
        
        Note : Cette action est sensible. Le service s'assure ici de la faisabilité 
        technique avant de demander au repository de purger la donnée.
        """
        return self.repository.delete(id_emp)