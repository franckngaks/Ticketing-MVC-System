from repository.employeRepository import EmployeRepository

class EmployeService:
    """
    COUCHE SERVICE : Intelligence et validation des règles Helpline.
    """
    def __init__(self):
        self.repository = EmployeRepository()

    def lister_employe(self):
        """Action : READ"""
        return self.repository.find_all()

    def inscrire_employe(self, nom, prenom, email, role, password="ChangeMe123!"):
        """Action : CREATE avec validation."""
        # On pourrait ajouter une règle ici : vérifier si l'email existe déjà
        return self.repository.save(nom, prenom, email, password, role)

    def mettre_a_jour_employe(self, id_emp, nom, prenom, email, role, password):
        """Action : UPDATE avec vérification de sécurité."""
        # RÈGLE MÉTIER : On vérifie si l'employé existe avant de tenter l'update
        if not self.repository.find_by_id(id_emp):
            print(f"⚠️ Erreur métier : L'ID #{id_emp} est inconnu.")
            return False
        
        return self.repository.update(id_emp, nom, prenom, email, password, role)

    def supprimer_employe(self, id_emp):
        """Action : DELETE (À utiliser avec prudence)."""
        return self.repository.delete(id_emp)