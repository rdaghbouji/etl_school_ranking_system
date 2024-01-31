from bs4 import BeautifulSoup
import requests
import pandas as pd





# Fonction pour extraire le statut (public ou privé) à partir d'une chaîne de caractères
def statut_str(string):
    substring = "Public"
    duree = "Durée"

    # Recherche des indices de début et de fin pour extraire la portion pertinente de la chaîne
    start_index = string.find(substring) + len("Public / Privé : ")
    end_index = string.find(duree)

    return string[start_index:end_index]





# Fonction pour extraire les données de statut d'une école à partir d'une URL
def get_statut(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    # Recherche de l'élément 'tbody', qui contient les données d'intérêt
    tab = doc.tbody

    # Recherche de tous les éléments 'tr' (ligne de tableau) dans 'tbody'
    trs = tab.find_all("tr")

    # Liste pour stocker les données extraites sous forme de dictionnaires
    data = []

    # Boucle à travers chaque élément 'tr' pour extraire les informations pertinentes
    for tr in trs:
        # Recherche de l'élément 'td' (cellule de tableau) avec le nom de classe spécifié
        nom_recup = tr.find("td", class_="tw-px-2 tw-py-4 sm:tw-p-4 tw-border tw-border-gray-600")

        # Recherche d'un élément 'tr' spécifique avec une classe indiquant des informations cachées
        hidden = tab.find("tr", class_="tw-hidden")
        
        # Extraction du contenu textuel de l'élément caché
        hidden_text = hidden.get_text(strip=True)
        
        # Appel de la fonction statut_str pour extraire le statut
        statut = statut_str(hidden_text)

        # Vérification si les deux éléments 'td' sont trouvés
        if nom_recup and statut:
            # Création d'une entrée de dictionnaire avec les informations extraites
            entry = {"Nom de l'école": nom_recup.get_text(strip=True),  "Public/Privé": statut}
            data.append(entry)

    # Création d'un DataFrame pandas à partir de la liste de dictionnaires
    df = pd.DataFrame(data)

    return df





# Fonction pour itérer à travers plusieurs pages et concaténer les DataFrames de statut
def set_statut():
    # URL initiale pour la première page
    url = "https://www.letudiant.fr/classements/classement-des-ecoles-d-ingenieurs.html"
    
    # Obtention des données pour la première page en utilisant la fonction get_statut
    page = get_statut(url)

    # Itération à travers des pages supplémentaires (de 2 à 9) et concaténation des DataFrames
    for i in range(2, 10):
        new_url = url + "?page=" + str(i)
        new_page = get_statut(new_url)
        page = pd.concat([page, new_page], ignore_index=True)

    # Retour du DataFrame final concaténé
    return page
