#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

def get_connection():
    """
    LOGIQUE TECHNIQUE : Établit le tunnel avec PHPMyAdmin (MySQL).
    
    Cette fonction est le point d'entrée unique pour tous les services 
    (Identity, Ticketing, etc.) souhaitant interagir avec les données.
    """
    try:
        # CONSEIL DÉBOGAGE : 
        # 1. Vérifiez que MySQL est "Vert" dans XAMPP/WAMP.
        # 2. Si 'localhost' échoue, essayez '127.0.0.1'.
        # 3. Vérifiez le port (3306 par défaut, parfois 3307 ou 3308).
        
        connection = mysql.connector.connect(
            host='127.0.0.1',    # '127.0.0.1' est souvent plus stable que 'localhost'
            port=8889,           # Vérifiez ce numéro dans votre panneau XAMPP
            user='root',         # Utilisateur par défaut
            password='root',         # Mot de passe vide par défaut
            database='helpline_db' # Nom de la base créée en SQL
        )
        
        if connection.is_connected():
            return connection
            
    except Error as e:
        # En cas d'erreur (serveur éteint, mauvais mot de passe...)
        print(f"❌ Erreur de connexion technique : {e}")
        print("👉 ASTUCE : Vérifiez que MySQL est bien lancé dans XAMPP/WAMP (bouton Start).")
        return None

# --- TEST D'INFRASTRUCTURE ---
# Ce bloc s'exécute uniquement si tu lances ce fichier directement.
if __name__ == "__main__":
    print("🔍 Test de la connexion à la base de données...")
    conn = get_connection()
    if conn:
        print("✅ Succès ! Le tunnel entre Python et PHPMyAdmin est opérationnel.")
        conn.close() # On libère la ressource immédiatement après le test
    else:
        print("⚠️ Échec. La base de données ne répond pas.")


