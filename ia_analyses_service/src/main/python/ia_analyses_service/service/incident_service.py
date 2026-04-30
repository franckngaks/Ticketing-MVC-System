def calculer_score_urgence(description):
    mots_cles = {
        "panne": 4, "crash": 5, "critique": 5, "bloqué": 4, 
        "erreur": 2, "lenteur": 2, "urgent": 5, "timeout": 3
    }
    
    score_total = 0
    description_lower = description.lower()
    
    for mot, poids in mots_cles.items():
        if mot in description_lower:
            score_total += poids
            
    # On plafonne le score à 10
    return min(score_total, 10)
