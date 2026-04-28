from flask import Flask, jsonify, request
from employe_service.controller.employe_controller import EmployeController

"""
APPLICATION FLASK : Micro-service Identity (Annuaire)
Mapping des routes REST pour la gestion des collaborateurs.
Port par défaut : 5000
"""

app = Flask(__name__)

# Initialisation du contrôleur MVC
# Le contrôleur gère lui-même son Service et son Repository
ctrl = EmployeController()

@app.route('/api/employes', methods=['GET'])
def get_employes():
    """Endpoint : Lister tous les collaborateurs (READ)"""
    resultat = ctrl.afficher_annuaire()
    return jsonify(resultat), 200

@app.route('/api/employes', methods=['POST'])
def post_employe():
    """Endpoint : Créer un nouveau profil (CREATE)"""
    data = request.get_json()
    reponse, status_code = ctrl.ajouter_collaborateur(data)
    return jsonify(reponse), status_code

@app.route('/api/employes/<int:id_emp>', methods=['PUT'])
def update_employe(id_emp):
    """Endpoint : Modifier un profil (UPDATE)"""
    data = request.get_json()
    reponse, status_code = ctrl.modifier_profil(id_emp, data)
    return jsonify(reponse), status_code

@app.route('/api/employes/<int:id_emp>', methods=['DELETE'])
def delete_employe(id_emp):
    """Endpoint : Supprimer un collaborateur (DELETE)"""
    reponse, status_code = ctrl.licencier_employe(id_emp)
    return jsonify(reponse), status_code

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 IDENTITY-SERVICE API est en ligne")
    print("📍 URL de base : http://127.0.0.1:5000/api/employes")
    print("="*50)
    
    # On force l'adresse 127.0.0.1 pour la stabilité sur Mac
    app.run(host='127.0.0.1', port=5000, debug=True)