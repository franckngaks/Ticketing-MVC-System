import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

print("--- DÉBUT DU SCRIPT ---")

# 1. Nouvelle syntaxe SQLAlchemy 2.0
class Base(DeclarativeBase):
    pass

# 2. Configuration (Vérifie bien le port 8889 pour MAMP)
DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1:8889/helpline_db"

print(f"Connexion cible : {DATABASE_URL}")

try:
    # 3. Création du moteur avec timeout court pour ne pas attendre 2h
    engine = create_engine(DATABASE_URL, connect_args={"connect_timeout": 5})
    
    # 4. Test réel avec une exécution SQL simple
    print("Tentative de ping MySQL...")
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ SUCCESS : La base de données répond présente !")
        
except Exception as e:
    print(f"❌ ERREUR CRITIQUE : {str(e)}")
    print("\n--- PISTES DE RÉSOLUTION ---")
    print("1. MySQL est-il lancé sur MAMP/XAMPP ?")
    print("2. Le port est-il bien 8889 ? (Vérifie dans les préférences MAMP)")
    print("3. La base 'helpline_db' existe-t-elle dans phpMyAdmin ?")

print("--- FIN DU SCRIPT ---")