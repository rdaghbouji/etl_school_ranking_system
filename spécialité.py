from bs4 import BeautifulSoup
import requests
import pandas as pd
from config_graphique import choix_des_spes
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


def get_url (spe) :
    url = "https://www.letudiant.fr/classements/classement-des-ecoles-d-ingenieurs.html?filters[677]="
    url_spe = f"{url}{spe}"
    return url_spe


def set_all_spe (): 

    spes_choisies = choix_des_spes ()

    for index, spe in enumerate(spes_choisies):
        url = get_url (spe)
        spe_df = set_spe (url, spe)
        if index == 0 :
            merged_df = spe_df
        else : 
            df = spe_df
            merged_df = pd.concat([merged_df, df], ignore_index=True)

# probleme spes_choisies = [] à résoudre

    result = merged_df.groupby("Nom de l'école")["Spécialité"].agg(custom_agg)

    return result