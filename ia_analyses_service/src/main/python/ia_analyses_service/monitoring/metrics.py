from prometheus_client import Gauge

# Définition de la jauge pour le score moyen
SCORE_URGENCE_MOYEN = Gauge('incident_avg_urgency_score', 'Moyenne des scores d urgence des incidents analysés')