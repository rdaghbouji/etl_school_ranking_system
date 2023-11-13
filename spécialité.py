from bs4 import BeautifulSoup
import requests
import pandas as pd
from autre import *




# Fonction pour extraire les données d'une spécialité à partir d'une URL et d'un nom de spécialité
def get_spe(url, nom_spe):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    tab = doc.tbody

    # Vérification si l'élément 'tbody' est trouvé
    if tab:
        trs = tab.find_all("tr")

        data = []

        # Boucle à travers chaque élément 'tr' pour extraire les informations pertinentes
        for tr in trs:
            # Recherche de l'élément 'td' (cellule de tableau) avec le nom de classe spécifié
            nom_recup = tr.find("td", class_="tw-px-2 tw-py-4 sm:tw-p-4 tw-border tw-border-gray-600")

            # Vérification si l'élément 'td' est trouvé
            if nom_recup:
                # Création d'une entrée de dictionnaire avec les informations extraites
                entry = {"Nom de l'école": nom_recup.get_text(strip=True), "Spécialité": nom_spe}
                data.append(entry)

        # Création d'un DataFrame pandas à partir de la liste de dictionnaires
        df = pd.DataFrame(data)

        return df





# Fonction pour itérer à travers plusieurs pages et concaténer les DataFrames de spécialités
def set_spe(url, nom_spe):
    # Obtention des données pour la première page
    page = get_spe(url, nom_spe)

    # Itération à travers des pages supplémentaires (de 2 à 3) et concaténation des DataFrames
    for i in range(2, 4):
        new_url = url + "&page=" + str(i)
        new_page = get_spe(new_url, nom_spe)
        page = pd.concat([page, new_page], ignore_index=True)

    # Retour du DataFrame final concaténé
    return page






# Fonction pour obtenir les données de toutes les spécialités
def set_all_spe():
    # URL pour différentes spécialités
    url1 = "https://www.letudiant.fr/classements/classement-des-ecoles-d-ingenieurs.html?filters[677]=Informatique"
    url2 = "https://www.letudiant.fr/classements/classement-des-ecoles-d-ingenieurs.html?filters%5B677%5D=Logiciels"
    url3 = "https://www.letudiant.fr/classements/classement-des-ecoles-d-ingenieurs.html?filters%5B677%5D=Ing%C3%A9nierie%20des%20syst%C3%A8mes%20d%27informations"

    # Obtention des données pour chaque spécialité
    spe1_df = set_spe(url1, "informatique")
    spe2_df = set_spe(url2, "logiciel")
    spe3_df = set_spe(url3, "ing des sys d'informations")

    # Concaténation des DataFrames de spécialités
    merged_df = pd.concat([spe1_df, spe2_df, spe3_df], ignore_index=True)

    # Agrégation des spécialités par nom d'école avec la fonction custom_agg
    result = merged_df.groupby("Nom de l'école")["Spécialité"].agg(custom_agg)

    return result
