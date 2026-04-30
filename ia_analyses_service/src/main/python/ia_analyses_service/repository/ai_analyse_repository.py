import pandas as pd
from sqlalchemy import create_engine

# Ta chaîne de connexion (que tu as validée)
engine = create_engine("mysql+pymysql://root:root@127.0.0.1:8889/helpline_db")

def recuperer_incidents():
    query = "SELECT id, titre, description FROM incidents"
    # On charge les données directement dans un DataFrame Pandas
    df = pd.read_sql(query, engine)
    return df

# Test de lecture
df_incidents = recuperer_incidents()
print(f"Nombre d'incidents à analyser : {len(df_incidents)}")