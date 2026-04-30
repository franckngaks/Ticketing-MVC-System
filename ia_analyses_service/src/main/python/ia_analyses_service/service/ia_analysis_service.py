from transformers import pipeline

class IAAnalysisService:
    def __init__(self):
        # On charge le modèle une seule fois au démarrage pour gagner du temps
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.categories = [
            "Network & Connectivity", 
            "Cloud & DevOps Infrastructure", 
            "Software & Application", 
            "Security & Identity"
        ]
        # Ton dictionnaire personnalisé
        self.poids_urgence = {
            "bsod": 5, "critical": 5, "panne": 4, "crash": 5, 
            "bloqué": 4, "urgent": 5, "timeout": 3,
            "panne": 4, "bloqué": 4, "urgent": 5, "climatisation": 5,
            # Anglais (Technique)
            "bsod": 5, "critical": 5, "crash": 5, "timeout": 3, 
            "failed": 3, "down": 4, "error": 2, "full": 3
        }

    def analyser_incident(self, description):
        # 1. Classification par l'IA
        res_ia = self.classifier(description, self.categories)
        categorie = res_ia['labels'][0]

        # 2. Sentiment (Nouveau)
        labels_sentiment = ["Frustré/Urgent", "Neutre", "Satisfait"]
        res_sent = self.classifier(description, labels_sentiment)
        sentiment = res_sent['labels'][0]
        
        # 3. Mots-clés (Nouveau - Logique simple pour commencer)
        # On extrait les mots de plus de 4 lettres qui sont dans ton dictionnaire
        mots_cles = [mot for mot in description.split() if len(mot) > 4 and mot.lower() in self.poids_urgence]
        mots_cles_str = ", ".join(mots_cles) if mots_cles else "Aucun"
        
        # 4. Score (déjà fait
        score = 0
        desc_clean = description.lower()
        for mot, poids in self.poids_urgence.items():
            if mot in desc_clean:
                score += poids
        
        return categorie, sentiment, mots_cles_str, min(score, 10)