import pandas as pd
from config_graphique import *


# Fonction pour attribuer une note selon le critère "Alternance"
def note_alternance(df, row):
    valeur_at = df.at[row, 'Alternance']
    if valeur_at == 'Oui':
        return 1
    else:
        return 0





# Fonction pour attribuer une note selon le critère "Spécialité"
def note_spe(df, row):
    valeur_at = df.at[row, 'Spécialité']
    if not pd.isna(valeur_at):
        return 1
    else:
        return 0





# Fonction pour attribuer une note selon le statut de l'école "Public/Privé"
def note_statut (df, row) :
    valeur_at = df.at[row, 'Public/Privé']
    if valeur_at == 'Public' :
        return 1 # Associe la note 1 si l'école est publique
    else :
        return 0 # Associe la note 1 si l'école est privée





# Fonction pour attribuer une note selon un critère donné
def note(df, row, critère):
    valeur_at = df.at[row, critère]
    end_index = valeur_at.find('/') # Récupère l'indice de "/" qui servira à récupérer la note 
    result = int(valeur_at[:end_index]) / int(valeur_at[end_index + 1:])
    return round(result, 2)






# Fonction principale pour calculer la note globale
def calc(df):
    notes = []
    coeff_choisis = choix_coeff ()
    for row in range(df.shape[0]):
        # Récupération des notes pour chaque critère
        alternance = note_alternance(df, row)
        spe = note_spe(df, row)
        statut = note_statut (df, row)
        formation = note(df, row, "Excellence académique")
        reseau = note(df, row, "Proximité avec les entreprises")
        international = note(df, row, "Ouverture internationale")
        
        # Calcul de la note globale selon la formule donnée (la formule peut être modifiée selon les préférences dans config.py)
        result = formule (alternance, spe, statut, formation, reseau, international, coeff_choisis)


        # Arrondi du résultat à deux décimales et ajout à la liste des notes
        notes.append(round(result, 2))

    return notes

