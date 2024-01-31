from get_set import *

def set_note_reseau () :
    url = "https://www.letudiant.fr/classements/classement-des-ecoles-d-ingenieurs/proximite-avec-les-entreprises.html"
    critere = "Proximité avec les entreprises"
    result = set (url, critere)
    return (result)



