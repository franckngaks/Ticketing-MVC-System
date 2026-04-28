from flask import Flask, jsonify, request
import requests

"""
ORCHESTRATEUR CENTRAL (API GATEWAY)
Ce service centralise les appels vers les microservices internes.
Structure : Maven-style (src/main/python)
"""

app = Flask(__name__)

# Configuration des URLs (On pourrait utiliser des variables d'environnement en prod)
IDENTITY_SERVICE_URL = "http://127.0.0.1:5000/api/employes"
TICKET_SERVICE_URL = "http://127.0.0.1:5001/api/tickets"

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard_data():
    """Agrégation de données Identity + Tickets."""
    try:
        # Récupération asynchrone simulée
        tickets = requests.get(TICKET_SERVICE_URL).json()
        employes_liste = requests.get(IDENTITY_SERVICE_URL).json()
        
        # Mapping pour recherche rapide
        employes_map = {e['id']: e for e in employes_liste}

        # Enrichissement des données (Data Enrichment)
        for t in tickets:
            user_id = t.get('id_createur')
            if user_id in employes_map:
                t['createur_info'] = {
                    "nom_complet": f"{employes_map[user_id]['prenom']} {employes_map[user_id]['nom']}",
                    "role": employes_map[user_id]['role']
                }

        return jsonify(tickets), 200

    except Exception as e:
        return jsonify({"error": "Service indisponible", "details": str(e)}), 502

@app.route('/api/proxy/tickets', methods=['POST'])
def create_ticket_secured():
    """Validation croisée avant transmission au service Ticket."""
    data = request.get_json()
    user_id = data.get('id_createur')

    # Vérification d'existence via le service Identity
    resp_identity = requests.get(IDENTITY_SERVICE_URL)
    valid_ids = [u['id'] for u in resp_identity.json()]

    if user_id not in valid_ids:
        return jsonify({"error": "ID Créateur inexistant"}), 403

    # Forward de la requête vers le Ticket Service
    resp = requests.post(TICKET_SERVICE_URL, json=data)
    return jsonify(resp.json()), resp.status_code

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🌐 API GATEWAY (INDUSTRIALISÉE) : PORT 8000")
    print("="*50)
    app.run(host='127.0.0.1', port=8000, debug=True)