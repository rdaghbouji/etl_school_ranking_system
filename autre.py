import pandas as pd

# Fonction personnalisée pour agréger les valeurs d'une colonne avec ' - ' comme séparateur
def custom_agg(x):
    return ' - '.join(x)

# Fonction pour fusionner plusieurs DataFrames sur la colonne "nom"
def merge(a, b, c, d, e, f):
    # Fusion des DataFrames successivement avec la méthode left join
    merged_df = pd.merge(a, b, on="nom", how='left')
    merged_df = pd.merge(merged_df, c, on="nom", how='left')
    merged_df = pd.merge(merged_df, d, on="nom", how='left')
    merged_df = pd.merge(merged_df, e, on="nom", how='left')
    merged_df = pd.merge(merged_df, f, on="nom", how='left')
    
    # Retour du DataFrame fusionné
    return merged_df
