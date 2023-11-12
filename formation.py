from bs4 import BeautifulSoup
import requests
import pandas as pd


# Fonction pour extraire les notes à partir de l'URL fournie
def get_note_formation(url):

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
        name = tr.find("td", class_="tw-px-2 tw-py-4 sm:tw-p-4 tw-border tw-border-gray-600")
        
        # Recherche de l'élément 'td' avec le nom de classe spécifié pour les notes
        note = tr.find("td", class_="tw-px-2 tw-py-4 sm:tw-p-4 tw-border tw-border-gray-600 tw-text-white tw-bg-indigo-500 tw-font-heading tw-font-normal tw-text-sm")

        # Vérification si les deux éléments 'td' sont trouvés
        if name and note:
            # Création d'une entrée de dictionnaire avec les informations extraites
            entry = {"nom": name.get_text(strip=True), "formation": note.get_text(strip=True)}
            data.append(entry)

    # Création d'un DataFrame pandas à partir de la liste de dictionnaires
    df = pd.DataFrame(data)

    # Retour du DataFrame final avec les notes
    return df
# Fonction pour récupérer les notes de formation à partir de plusieurs pages

def set_note_formation():
    # URL initiale pour la première page
    url = "https://www.letudiant.fr/classements/classement-des-ecoles-d-ingenieurs/excellence-academique.html"
    
    # Obtention des notes de la première page en utilisant la fonction get_note
    page = get_note_formation(url)

    # Itération à travers des pages supplémentaires (de 2 à 9) et concaténation des DataFrames
    for i in range(2, 10):
        new_url = url + "?page=" + str(i)
        new_page = get_note_formation(new_url)
        page = pd.concat([page, new_page], ignore_index=True)

    # Retour du DataFrame final avec les notes de formation
    return page
