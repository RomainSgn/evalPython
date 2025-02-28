class Livre:
    def __init__(self, titre, auteur, annee_publication, disponibilite):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.disponibilite = disponibilite
    
    def __str__(self):
        if self.disponibilite:
            return(f"- Titre : {self.titre}\n- Auteur : {self.auteur}\n- Année de publication : {self.annee_publication}\n- Disponnibilité : Disponible")
        else:
            return(f"- Titre : {self.titre}\n- Auteur : {self.auteur}\n- Année de publication : {self.annee_publication}\n- Disponnibilité : Indisponible")

class LivreEmpruntable(Livre):
    def emprunter_livre(self):
        if self.disponibilite:
            self.disponibilite = False
            return("Le livre à été emprunter !")
        else:
            return("Impossible d'enprunter ce livre")
        
    def retourner_livre(self):
        if self.disponibilite == False:
            self.disponibilite = True
            return("Le livre à été retourné")
        else:
            return("Impossible de retourner un livre non-emprunter !")

livre1 = LivreEmpruntable("Fire and Blood", "George R.R. Martin", 2018, True)
print(livre1)
print(livre1.emprunter_livre())
print(livre1)
print(livre1.retourner_livre())
