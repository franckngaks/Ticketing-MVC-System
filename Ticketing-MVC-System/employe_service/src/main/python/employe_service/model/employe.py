class Employe:
    """
    CLASSE MODÈLE : Représente l'entité 'Employé' du système Helpline.
    
    Dans le pattern MVC, le Modèle est une représentation fidèle des données 
    en mémoire vive. Il sert de conteneur de transport pour déplacer les 
    informations entre la base de données (Repository) et l'affichage (Vue).
    """

    def __init__(self, id, nom, prenom, email, role, password_hash=None):
        """
        CONSTRUCTEUR : Initialise une instance d'un collaborateur.
        
        Args:
            id (int): Identifiant unique provenant de la base de données.
            nom (str): Nom de famille de l'employé.
            prenom (str): Prénom de l'employé.
            email (str): Adresse email professionnelle (sert d'identifiant de connexion).
            role (str): Niveau d'accès (ex: 'User', 'Tech', 'Admin').
            password_hash (str, optional): Empreinte sécurisée du mot de passe.
        """
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.role = role
        self.password_hash = password_hash

    @classmethod
    def from_dict(cls, data):
        """
        FACTORY METHOD (Méthode de fabrique) :
        Permet de créer un objet 'Employe' directement à partir d'un 
        dictionnaire renvoyé par une requête SQL (cursor.fetchone()).
        
        Cette méthode facilite la conversion entre le monde relationnel (SQL) 
        et le monde objet (Python).
        
        Args:
            data (dict): Dictionnaire contenant les clés correspondant aux colonnes SQL.
            
        Returns:
            Employe: Une nouvelle instance de la classe initialisée avec les données.
        """
        return cls(
            id=data.get('id'),
            nom=data.get('nom'),
            prenom=data.get('prenom'),
            email=data.get('email'),
            role=data.get('role'),
            password_hash=data.get('password_hash')
        )