from flask import Flask, jsonify, request
from incident_service.controller.incident_controller import IncidentController

"""
APPLICATION FLASK : Serveur Web du Micro-service Ticket.
Ce fichier réalise le mapping entre les requêtes HTTP (Talend) 
et la logique métier du Contrôleur.
"""

app = Flask(__name__)

# Initialisation du contrôleur (Architecture MVC)
ctrl = IncidentController()

@app.route('/api/tickets', methods=['GET'])
def get_tickets():
    """
    MAPPING GET : Récupérer la liste des incidents.
    URL : http://127.0.0.1:5001/api/tickets
    """
    try:
        incidents = ctrl.lister_tous_les_incidents()
        return jsonify(incidents), 200
    except Exception as e:
        return jsonify({"error": "Erreur lors de la lecture", "details": str(e)}), 500

@app.route('/api/tickets', methods=['POST'])
def post_ticket():
    """
    MAPPING POST : Ouvrir un nouveau ticket.
    URL : http://127.0.0.1:5001/api/tickets
    """
    data = request.get_json()
    
    # On délègue la création au contrôleur
    reponse, status_code = ctrl.creer_nouvel_incident(data)
    
    return jsonify(reponse), status_code

@app.route('/api/tickets/<int:id_ticket>', methods=['PUT'])
def update_ticket(id_ticket):
    """
    MAPPING PUT : Modifier les informations d'un ticket (Titre, Prio, Desc).
    URL : http://127.0.0.1:5001/api/tickets/ID
    Body (JSON) : {"titre": "...", "priorite": "...", "description": "..."}
    """
    data = request.get_json()
    
    # On appelle la méthode de modification du contrôleur
    # Note: Cette méthode doit exister dans ton incident_controller.py
    reponse, status_code = ctrl.modifier_ticket_existant(id_ticket, data)
    
    return jsonify(reponse), status_code

@app.route('/api/tickets/<int:id_ticket>/resolve', methods=['PUT'])
def resolve_ticket(id_ticket):
    """
    MAPPING PUT : Résoudre un incident spécifique.
    URL : http://127.0.0.1:5001/api/tickets/ID/resolve
    """
    data = request.get_json()
    
    # Passage de l'ID et du technicien au contrôleur
    reponse, status_code = ctrl.resoudre_un_incident(id_ticket, data)
    
    return jsonify(reponse), status_code

if __name__ == '__main__':
    print("="*50)
    print("🚀 HELPLINE - TICKET SERVICE API (Flask)")
    print("📍 URL de base : http://127.0.0.1:5001/api/tickets")
    print("="*50)
    
    # Utilisation du port 5001 pour l'isolation micro-service
    app.run(port=5001, debug=True)