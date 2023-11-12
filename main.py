
from formation import *
from reseau import *
from international import *
from alternance import *
from statut import *
from spécialité import *  
from autre import *

# Obtention des données de notes de formation
formation_df = set_note_formation()

# Obtention des données du réseau
reseau_df = set_note_reseau()

# Obtention des données internationales
international_df = set_note_international()

# Obtention des données en alternance
alternance_df = set_alternance()

# Obtention des données de statut
statut_df = set_statut()

# Obtention des données de spécialité
spe_df = set_all_spe()

# Fusion de tous les DataFrames obtenus
data = merge(formation_df, reseau_df, international_df, alternance_df, statut_df, spe_df)

# Affichage du DataFrame final
data.to_excel('db.xlsx')
