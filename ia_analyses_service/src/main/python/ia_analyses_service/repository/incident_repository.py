from sqlite3 import IntegrityError

import pandas as pd
from sqlalchemy import text

class IncidentRepository:
    def __init__(self, engine):
        # On injecte l'engine de connexion défini dans ta config
        self.engine = engine

    def get_global_stats(self):
        """Récupère la somme des scores et le nombre total d'analyses en base."""
        query = text("""
            SELECT SUM(score_urgence) as total_score, COUNT(*) as total_count 
            FROM ia_analyses
        """)
        with self.engine.connect() as conn:
            result = conn.execute(query).fetchone()
            # On gère le cas où la table est vide (retourne 0 au lieu de None)
            return {
                "sum": result.total_score or 0,
                "count": result.total_count or 0
            }

    def get_all_descriptions(self):
        """Récupère les incidents qui n'ont pas encore de correspondance dans ia_analyses."""
        # On sélectionne les colonnes de la table incidents (alias 'i')
        # qui n'ont pas de correspondance dans ia_analyses (alias 'a')
        query = """
            SELECT i.id, i.titre, i.description 
            FROM incidents i
            LEFT JOIN ia_analyses a ON i.id = a.id_incident
            WHERE a.id_incident IS NULL
        """
        
        # On utilise pandas pour lire le résultat directement dans un DataFrame
        return pd.read_sql(query, self.engine)

    def save_analysis(self, id_incident, categorie, sentiment, mots_cles, score):
        query = text("""
            INSERT INTO ia_analyses (id_incident, categorie_predite, sentiment_utilisateur, mots_cles_extraits, score_urgence, date_analyse)
            VALUES (:id, :categorie, :sentiment, :mots, :score, NOW())
        """)
        
        try:
            with self.engine.connect() as conn:
                conn.execute(query, {
                    "id": id_incident, 
                    "categorie": categorie, 
                    "sentiment": sentiment, 
                    "mots": mots_cles, 
                    "score": score
                })
                conn.commit()
        except IntegrityError:
            # On attrape l'erreur si l'ID_INCIDENT existe déjà
            print(f"⚠️  L'incident #{id_incident} est déjà présent dans la base. Skip.")