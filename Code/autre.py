import pandas as pd
from sqlalchemy import create_engine




# Fonction personnalisée pour agréger les valeurs d'une colonne avec ' - ' comme séparateur
def custom_agg(x):
    return ' - '.join(x)





# Fonction pour fusionner plusieurs DataFrames sur la colonne "Nom de l'école"
def merge(a, b, c, d, e, f):
    # Fusion des DataFrames successivement avec la méthode left join
    merged_df = pd.merge(a, b, on="Nom de l'école", how='left')
    merged_df = pd.merge(merged_df, c, on="Nom de l'école", how='left')
    merged_df = pd.merge(merged_df, d, on="Nom de l'école", how='left')
    merged_df = pd.merge(merged_df, e, on="Nom de l'école", how='left')
    merged_df = pd.merge(merged_df, f, on="Nom de l'école", how='left')
    
    # Retour du DataFrame fusionné
    return merged_df






def data_to_sql(data):
    # Database connection URL
    db_url = 'sqlite:///database.db'
    engine = create_engine(db_url)

    # Append the new DataFrame to the existing database table
    data.to_sql('tab', con=engine, index=False, if_exists='replace')

    # Read the updated data from the database
    df_from_db = pd.read_sql('tab', con=engine)
    
    return df_from_db




