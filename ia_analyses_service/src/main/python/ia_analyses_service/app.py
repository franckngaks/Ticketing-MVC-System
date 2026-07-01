import time
from prometheus_client import start_http_server

# Imports corrigés et harmonisés par rapport à la racine du service
from config.database import engine
from service.incident_manager import IncidentManager

def run_pipeline():
    # 1. Initialisation du "Chef d'Orchestre"
    manager = IncidentManager(engine)
    
    print("🚀 Démarrage du système d'analyse IA...")
    
    # 2. Lancement du cycle complet : Lecture -> Analyse -> Sauvegarde
    manager.executer_analyse_complete()
    
    print("✅ Traitement terminé avec succès !")

if __name__ == "__main__":
    # Lancement du serveur de métriques AVANT de lancer le pipeline
    # Port 8000 pour Prometheus
    start_http_server(8000)
    print("📊 Serveur de métriques disponible sur http://localhost:8000/metrics")
    
    run_pipeline()

    print("😴 Analyse terminée. Le serveur reste actif pour Prometheus (Ctrl+C pour stopper)...")
    while True:
        time.sleep(1) # Garde le script allumé indéfiniment pour que Prometheus puisse scrapper les données