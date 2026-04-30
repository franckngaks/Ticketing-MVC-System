#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

def get_connection():
    """
    Établit une connexion sécurisée avec la base de données MySQL.
    Configuration optimisée pour MAMP sur macOS.
    """
    try:
        # Tentative de connexion avec les paramètres fournis
        connection = mysql.connector.connect(
            host='127.0.0.1',      # IP locale pour plus de stabilité
            port=8889,             # Port par défaut de MAMP SQL
            user='root',           # Administrateur par défaut
            password='root',       # Mot de passe par défaut MAMP
            database='helpline_db' # Nom de ta base de données
        )

        if connection.is_connected():
            return connection

    except Error as e:
        # Journalisation de l'erreur pour la maintenance applicative
        print(f"❌ Erreur de connexion à MySQL : {e}")
        return None

# --- TEST D'AUTO-VALIDATION ---
if __name__ == "__main__":
    print("⏳ Test de connexion en cours...")
    conn = get_connection()
    if conn:
        print("✅ Connexion établie avec succès !")
        conn.close()
    else:
        print("❌ Échec : Vérifiez que les serveurs MAMP sont bien lancés.")


