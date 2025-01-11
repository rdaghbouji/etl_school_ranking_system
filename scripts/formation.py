from get_set import *

def set_note_formation ():
    url = "https://www.letudiant.fr/classements/classement-des-ecoles-d-ingenieurs/excellence-academique.html"
    critere = "Excellence académique"
    result = set (url, critere)
    return result


