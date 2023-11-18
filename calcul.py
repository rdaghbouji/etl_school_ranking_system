import pandas as pd





# Fonction pour attribuer une note en fonction du critère "Alternance"
def note_alternance(df, row):
    valeur_at = df.at[row, 'Alternance']
    if valeur_at == 'Oui':
        return 1
    else:
        return 0





# Fonction pour attribuer une note en fonction du critère "Spécialité"
def note_spe(df, row):
    valeur_at = df.at[row, 'Spécialité']
    if not pd.isna(valeur_at):
        return 1
    else:
        return 0





# Fonction pour calculer la note en fonction du critère "Proximité avec les entreprises"
def note_reseau(df, row):
    valeur_at = df.at[row, 'Proximité avec les entreprises']
    end_index = valeur_at.find('/')
    result = int(valeur_at[:end_index]) / 30
    return round(result, 2)





# Fonction pour calculer la note en fonction du critère "Ouverture internationale"
def note_international(df, row):
    valeur_at = df.at[row, 'Ouverture internationale']
    end_index = valeur_at.find('/')
    result = int(valeur_at[:end_index]) / 40
    return round(result, 2)





# Fonction pour calculer la note en fonction du critère "Excellence académique"
def note_formation(df, row):
    valeur_at = df.at[row, 'Excellence académique']
    end_index = valeur_at.find('/')
    result = int(valeur_at[:end_index]) / 30
    return round(result, 2)




# Fonction principale pour calculer la note globale
def calc(df):
    notes = []
    for row in range(df.shape[0]):
        # Récupération des notes pour chaque critère
        alternance = note_alternance(df, row)
        reseau = note_reseau(df, row)
        formation = note_formation(df, row)
        international = note_international(df, row)
        spe = note_spe(df, row)

        # Calcul de la note globale selon la formule donnée
        result = 4 * (float(alternance) + float(spe)) + 5 * float(reseau) + 4 * float(formation) + float(international)
        # Arrondi du résultat à deux décimales et ajout à la liste des notes
        notes.append(round(result, 2))

    return notes

