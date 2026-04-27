class Incident:
    """
    CLASSE MODÈLE : Représente la structure d'un incident en mémoire.
    Ne contient aucune logique SQL, juste des attributs.
    """
    def __init__(self, id, titre, priorite, statut, description, id_createur):
        self.id = id
        self.titre = titre
        self.priorite = priorite
        self.statut = statut
        self.description = description
        self.id_createur = id_createur