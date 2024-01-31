import tkinter as tk




class CoefficientsWindow:
    def __init__(self):
        description_text = """
        NB : 
        - Toutes les notes varient entre 0 et 1.
        - Pour les critères alternance, statut et spécialités les notes sont bianires :
            Alternance = 1 : il y a possibilité d'alternance d'alternance.
            Statut = 1 : l'école est publique.
            Spécialité = 1 : l'école propose au moins une des spécialités choisies.
        Recommendations :
        - Choisir des coefficients tels que leur total soit égal à 20. 
        - Associer les coefficients les plus grands aux critères les plus importants.
        """
        self.window = tk.Tk()
        self.window.title("Choix des Coefficients")
        self.coeff_names = ["Excellence académique", "Proximité avec les entreprises", "Ouverture internationale", "Alternance", "Public/Privé", "Spécialité"]
        self.labels_coeffs = [tk.Label(self.window, text=coeff_name) for coeff_name in self.coeff_names]
        self.entry_coeffs = [tk.Entry(self.window) for _ in range(6)]
        self.label_debut = tk.Label(self.window, text="Choisissez vos coefficients :")
        self.button_valider = tk.Button(self.window, text="Valider", command=self.choix_coeff)
        self.label_description = tk.Label(self.window, text=description_text, wraplength=400, justify="left")
        self.label_result = tk.Label(self.window, text="Coefficients choisis :")

        # Ajout des attributs de classe
        self.liste_coeff = []

        self.setup_ui()



    def setup_ui(self):
        self.label_debut.grid(row=0, column=0, columnspan=6)
        for i, (label_coeff, entry_coeff) in enumerate(zip(self.labels_coeffs, self.entry_coeffs)):
            label_coeff.grid(row=1, column=i)
            entry_coeff.grid(row=2, column=i)
        self.label_description.grid(row=3, column=0, columnspan=6)
        self.button_valider.grid(row=12, column=0, columnspan=6)
        self.label_result.grid(row=13, column=0, columnspan=6)



    def choix_coeff(self):
        # Utiliser l'attribut de classe pour stocker les coefficients choisis
        self.liste_coeff = [float(entry_coeff.get()) for entry_coeff in self.entry_coeffs]
        self.label_result.config(text=f"Coefficients choisis : {self.liste_coeff}")

        # Vous pouvez ajouter ici l'appel à la fonction formule avec les coefficients choisis
        # Exemple : formule(alternance, spe, statut, formation, reseau, international, self.liste_coeff)

        return self.liste_coeff



    def run(self):
        self.window.mainloop()
        




class SpesWindow:
    def __init__(self, spes_disponibles):
        self.window = tk.Tk()
        self.window.title("Choix des Spes")

        self.spes_disponibles = spes_disponibles
        self.spes_choisies = []

        self.listbox_spes = tk.Listbox(self.window, selectmode=tk.MULTIPLE)
        for spe in self.spes_disponibles:
            self.listbox_spes.insert(tk.END, spe)

        self.button_ajouter = tk.Button(self.window, text="Ajouter une spe", command=self.ajouter_spes)
        self.label_resultat = tk.Label(self.window, text="Spes choisies :")

        self.setup_ui()



    def setup_ui(self):
        self.listbox_spes.grid(row=0, column=0, padx=10, pady=10)
        self.button_ajouter.grid(row=1, column=0, padx=10, pady=10)
        self.label_resultat.grid(row=2, column=0, padx=10, pady=10)



    def ajouter_spes(self):
        selected_indices = self.listbox_spes.curselection()
        self.spes_choisies = [self.spes_disponibles[index] for index in selected_indices]
        self.label_resultat.config(text=f"Spes choisies : {', '.join(self.spes_choisies)}")



    def run(self):
        self.window.mainloop()





def choix_coeff () :
    coefficients_window = CoefficientsWindow()
    coefficients_window.run()

    # Accéder aux valeurs des attributs de classe depuis l'instance de la classe
    liste_coeff = coefficients_window.liste_coeff
    print("Coefficients choisis :", liste_coeff)

    return liste_coeff





def choix_des_spes () :
    specialites_disponibles = [
    'Agriculture', 'Architecture', 'Autres', 'Bâtiment', 'Biochimique et biomoléculaire',
    'Bioingénierie', 'Biomédical', 'Céramique industrielle', 'Forêt et génie des biosystèmes',
    'Génie agroalimentaire', 'Génie biologique', 'Génie civil', 'Génie des matériaux',
    'Génie électrique et électronique', 'Génie électromécanique', 'Génie environnemental',
    'Génie industriel', 'Génie nucléaire', 'Génie optique et photonique', 'Géologie',
    'Informatique', 'Ingénierie aérospatiale et aéronautique', 'Ingénierie chimique',
    'Ingénierie des systèmes', "Ingénierie des systèmes d'informations", 'Ingénierie topographique',
    'Ingénieur généraliste', 'Ingénieur manager', 'Logiciels', 'Télécommunications']


    spes_window = SpesWindow(specialites_disponibles)
    spes_window.run()

    # Accéder aux valeurs des attributs de classe depuis l'instance de la classe
    spes_choisies = spes_window.spes_choisies
    print("Spes choisies :", spes_choisies)

    return spes_choisies





def formule (alternance, spe, statut, formation, reseau, international, liste_coeff) :
    formule = liste_coeff[0] * float(formation) + liste_coeff[1] * float(reseau) + liste_coeff[2] * float(international) + liste_coeff[3] * float(alternance) + liste_coeff[4] * float(statut) + liste_coeff[5] * float(spe)
    return formule

