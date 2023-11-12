from get_note import *

def set_note_vie_etudiante ():
    url = "https://www.letudiant.fr/classements/classement-des-villes-etudiantes/emploi.html?filters%5B883%5D=Plus%20de%2040%20000"
    data = get_note(url)

    return data
