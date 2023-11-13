from get_set import *

def set_note_international () :
    url = "https://www.letudiant.fr/classements/classement-des-ecoles-d-ingenieurs/ouverture-internationale.html"
    critere = "Ouverture internationale"
    result = set (url, critere)
    return result



