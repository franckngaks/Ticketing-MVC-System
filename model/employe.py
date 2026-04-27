class Employe:
    """
    CLASSE MODÈLE : Représente la structure d'un collaborateur.
    Sert à transporter les données entre les couches.
    """
    def __init__(self, id, nom, prenom, email, role, password_hash=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.role = role
        self.password_hash = password_hash

    @classmethod
    def from_dict(cls, data):
        """Transforme un dictionnaire SQL en objet Employe."""
        return cls(
            id=data.get('id'),
            nom=data.get('nom'),
            prenom=data.get('prenom'),
            email=data.get('email'),
            role=data.get('role'),
            password_hash=data.get('password_hash')
        )