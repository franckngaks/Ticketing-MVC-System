from service.employeService import EmployeService

class EmployeController:
    """
    CONTRÔLEUR : Gère les interactions liées aux employés.
    Fait le pont entre l'interface utilisateur et le service Identity.
    """
    def __init__(self):
        # Initialisation du service associé
        self.service = EmployeService()

    def afficher_annuaire(self):
        """
        Action : READ
        Récupère la liste des collaborateurs et l'envoie à la 'Vue' (ici le terminal).
        """
        print("\n👥 --- ANNUAIRE DES COLLABORATEURS ---")
        employes = self.service.lister_employe()
        
        if not employes:
            print("L'annuaire est actuellement vide.")
        else:
            for e in employes:
                # Formatage de l'affichage pour l'utilisateur
                print(f"ID #{e['id']} | {e['prenom']} {e['nom']} ({e['role']})")

    def ajouter_collaborateur(self, nom, prenom, email, role):
        """
        Action : CREATE
        Demande au service d'inscrire un nouvel employé en base.
        """
        print(f"\n✨ Inscription de {prenom} {nom}...")
        id_genere = self.service.inscrire_employe(nom, prenom, email, role)
        
        if id_genere:
            print(f"✅ Succès : Collaborateur enregistré avec l'ID #{id_genere}.")
            return id_genere
        else:
            print("❌ Échec : Les informations fournies sont invalides ou l'email existe déjà.")
            return None

    def modifier_profil(self, id_emp, nom, prenom, email, role, password):
        """
        Action : UPDATE
        Lance la mise à jour des informations d'un employé existant.
        """
        print(f"\n📝 Mise à jour du profil #{id_emp}...")
        if self.service.mettre_a_jour_employe(id_emp, nom, prenom, email, role, password):
            print(f"✅ Les modifications pour l'employé #{id_emp} ont été enregistrées.")
        else:
            print(f"❌ Erreur : Impossible de modifier l'employé #{id_emp}.")

    def licencier_employe(self, id_emp):
        """
        Action : DELETE
        Demande la suppression définitive d'un compte utilisateur.
        """
        print(f"\n⚠️ Tentative de suppression du profil #{id_emp}...")
        if self.service.supprimer_employe(id_emp):
            print(f"✅ Le profil #{id_emp} a été retiré de l'organisation.")
        else:
            print(f"❌ Action refusée : L'ID #{id_emp} est introuvable ou possède des tickets liés.")