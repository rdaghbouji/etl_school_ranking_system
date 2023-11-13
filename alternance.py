# Importation des bibliothèques nécessaires pour le web scraping et la manipulation des données
from bs4 import BeautifulSoup
import requests
import pandas as pd




# Fonction pour extraire la sous-chaîne indiquant s'il s'agit d'un programme en "Alternance"
def alternance_str(string):
    substring = "Alternance"

    # Recherche de l'indice de début et de fin pour extraire la portion pertinente de la chaîne
    start_index = string.find(substring) + len("Alternance : ")
    end_index = start_index + len("Oui")

    return string[start_index:end_index]






# Fonction pour extraire les données de l'URL fournie et créer un DataFrame
def get_alternance(url):
    # Envoi d'une requête HTTP GET à l'URL spécifiée
    result = requests.get(url)

    # Analyse du contenu HTML de la page à l'aide de BeautifulSoup
    doc = BeautifulSoup(result.text, "html.parser")

    # Extraction de l'élément 'tbody', qui contient les données d'intérêt
    tab = doc.tbody

    # Recherche de tous les éléments 'tr' (ligne de tableau) dans 'tbody'
    trs = tab.find_all("tr")

    # Liste pour stocker les données extraites sous forme de dictionnaires
    data = []

    # Boucle à travers chaque élément 'tr' pour extraire les informations pertinentes
    for tr in trs:
        # Recherche de l'élément 'td' (cellule de tableau) avec le nom de classe spécifié
        nom_recup = tr.find("td", class_="tw-px-2 tw-py-4 sm:tw-p-4 tw-border tw-border-gray-600")  # Mettez à jour avec le bon nom de classe

        # Vérification si l'élément 'td' est trouvé
        if nom_recup:
            # Recherche d'un élément 'tr' spécifique avec une classe indiquant des informations cachées
            hidden = tab.find("tr", class_="tw-hidden")
            
            # Extraction du contenu textuel de l'élément caché
            hidden_text = hidden.get_text(strip=True)
            
            # Appel de la fonction alternance_str pour extraire la sous-chaîne 'Alternance'
            alternance = alternance_str(hidden_text)

            # Création d'une entrée de dictionnaire avec les informations extraites
            entry = {"Nom de l'école": nom_recup.get_text(strip=True), "Alternance": alternance}
            data.append(entry)

    # Création d'un DataFrame pandas à partir de la liste de dictionnaires
    df = pd.DataFrame(data)
    return df





# Fonction pour itérer à travers plusieurs pages et concaténer les DataFrames
def set_alternance():
    # URL initiale pour la première page
    url = "https://www.letudiant.fr/classements/classement-des-ecoles-d-ingenieurs/excellence-academique.html"
    
    # Obtention des données pour la première page
    page = get_alternance(url)

    # Itération à travers des pages supplémentaires (de 2 à 9) et concaténation des DataFrames
    for i in range(2, 10):
        new_url = url + "?page=" + str(i)
        new_page = get_alternance(new_url)
        page = pd.concat([page, new_page], ignore_index=True)

    # Retour du DataFrame final concaténé
    return page

