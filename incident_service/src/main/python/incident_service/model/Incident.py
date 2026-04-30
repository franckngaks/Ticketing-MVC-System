class Incident:
    """
    CLASSE MODÈLE : Représente la structure d'un incident en mémoire.
    
    Dans le pattern MVC, cette classe est une 'Entité'. Elle sert de 
    conteneur de données standardisé pour transporter les informations 
    entre le Repository (Base de données) et le Contrôleur.
    """

    def __init__(self, id, titre, priorite, statut, description, id_createur):
        """
        CONSTRUCTEUR : Initialise un objet Incident.
        
        Args:
            id (int): Identifiant unique du ticket.
            titre (str): Résumé du problème.
            priorite (str): Niveau d'urgence (Basse, Moyenne, Haute, Critique).
            statut (str): État du workflow (Ouvert, En cours, Résolu).
            description (str): Détails techniques du problème.
            id_createur (int): ID de l'employé ayant ouvert le ticket.
        """
        self.id = id
        self.titre = titre
        self.priorite = priorite
        self.statut = statut
        self.description = description
        self.id_createur = id_createur

    @classmethod
    def from_dict(cls, data):
        """
        MÉTHODE DE CLASSE (Factory) :
        Pourquoi cette méthode est importante ? 
        Elle permet de créer une instance d'Incident directement à partir 
        d'un dictionnaire renvoyé par un curseur SQL (cursor.fetchone()).
        
        Cela évite de devoir extraire manuellement chaque champ dans le 
        Repository et rend le code beaucoup plus propre et maintenable.
        
        Args:
            data (dict): Le dictionnaire de données provenant de MySQL.
            
        Returns:
            Incident: Une instance de la classe proprement typée.
        """

        """.get() dans la méthode de classe évite que l'application ne plante 
        si une colonne est manquante dans le résultat SQL.
        """
        return cls(
            id=data.get('id'),
            titre=data.get('titre'),
            priorite=data.get('priorite'),
            statut=data.get('statut'),
            description=data.get('description'),
            id_createur=data.get('id_createur')
        )