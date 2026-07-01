from ia_analyses_service.repository.incident_repository import IncidentRepository
from ia_analyses_service.service.ia_analysis_service import IAAnalysisService
from ia_analyses_service.monitoring.metrics import SCORE_URGENCE_MOYEN

class IncidentManager:
    def __init__(self, engine):
        # On prépare nos outils
        self.repo = IncidentRepository(engine)
        self.ia_service = IAAnalysisService()

    def executer_analyse_complete(self):
        # On récupère tous les incidents via le repository
        df_incidents = self.repo.get_all_descriptions() # cite: 1
        
        print(f"📊 {len(df_incidents)} incidents détectés. Lancement de l'IA...\n")
        print("-" * 50)

        # Dans ton IncidentManager
        total_score = 0
        count = 0

        for _, row in df_incidents.iterrows():
            # 🚨 SÉCURITÉ ANTI-CRASH : On extrait et nettoie la description et le titre
            titre_brut = str(row['titre']) if 'titre' in row and row['titre'] else "Sans titre"
            desc_brute = str(row['description']) if 'description' in row and row['description'] else ""
            
            # Si la description est vide ou équivalente à 'nan' (chaîne générée par Pandas), on prend le titre
            if not desc_brute.strip() or desc_brute.lower() == 'nan':
                description_propre = titre_brut
            else:
                description_propre = desc_brute

            # 1. Analyse par le service IA (avec la description sécurisée)
            categorie, sentiment, mots_cles, score = self.ia_service.analyser_incident(description_propre)

            # 1. Mise à jour des compteurs
            total_score += score
            count += 1
            
            # 2. Calcul de la moyenne actuelle
            moyenne_actuelle = total_score / count
            
            # 3. Mise à jour de la métrique Prometheus
            SCORE_URGENCE_MOYEN.set(moyenne_actuelle)
            
            # 2. Ton PRINT demandé : Le rapport d'analyse
            print(f"🆔 Incident #{row['id']}")
            print(f"📝 Panne : {titre_brut}")
            print(f"🤖 Analyse IA : {categorie}")
            print(f"🤖 Sentiment de l'utilisateur: {sentiment}")
            print(f"🤖 Mots clés extraits : {mots_cles}")
            print(f"⚠️ Score Urgence : {score}/10")
            print("-" * 50)

            # 3. Sauvegarde dans ia_analyses
            self.repo.save_analysis(row['id'], categorie, sentiment, mots_cles, score)