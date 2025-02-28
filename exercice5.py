import math  # Importation du module math
def verification(montant):
    if montant % 10 != 0:  # Vérification si le montant est un multiple de 10
        message = "Le montant doit être un multiple de 10 !"
        return message
    else:
        if montant > 500:  # Vérification que le montant ne dépasse pas 500
            message = "Le montant ne doit pas dépasser 500 (limite de retrait)"
            return message
        else:
            if montant >= 50:
                nb50 = math.floor(montant / 50)  # Divise par 50 arrondi vers le bas pour avoir le nombre de billets de 50
                montant -= (50*nb50)  # Je diminue le montant des billets de 50
                if montant >= 20:  # Je vérifie que le montant restant est supérieur ou égal à 20
                    nb20 = math.floor(montant / 20)  # Divise par 20 arrondi vers le bas pour avoir le nombre de billets de 20
                    montant -= (20*nb20)  # Je diminue le montant des billets de 20
                    if montant >= 10:  # Je vérifie que le montant restant est supérieur ou égal à 10
                        nb10 = 1  # Mathématiquement il ne reste forcément que 1 billet de 10 à ajouter
                        if nb50 > 1 and nb20 > 1:  # Vérification du nombre de billet pour affichage au pluriel ou singulier
                            return(f"Billets distribués:\n- {nb50} billets de 50€\n- {nb20} billets de 20€\n- {nb10} billet de 10€")
                        elif nb50 > 1 and nb20 == 1:
                            return(f"Billets distribués:\n- {nb50} billets de 50€\n- {nb20} billet de 20€\n- {nb10} billet de 10€")
                        else:
                            return(f"Billets distribués:\n- {nb50} billet de 50€\n- {nb20} billet de 20€\n- {nb10} billet de 10€")
                    else:  # Pas de billet de 10€
                        if nb50 > 1 and nb20 > 1:
                            return(f"Billets distribués:\n- {nb50} billets de 50€\n- {nb20} billets de 20€")
                        elif nb50 > 1 and nb20 == 1:
                            return(f"Billets distribués:\n- {nb50} billets de 50€\n- {nb20} billet de 20€")
                        elif nb50 == 1 and nb20 > 1:
                            return(f"Billets distribués:\n- {nb50} billets de 50€\n- {nb20} billets de 20€")
                        else:
                            return(f"Billets distribués:\n- {nb50} billet de 50€\n- {nb20} billet de 20€")
                elif montant == 10:  # Pas de billets de 20€ 
                    nb10 = 1
                    return(f"Billets distribués:\n- {nb50} billets de 50€\n- {nb10} billet de 10€")
                else:  # Que des billets de 50€
                    if nb50 > 1:
                        return(f"Billets distribués:\n- {nb50} billets de 50€")
                    else:
                        return(f"Billet distribué:\n- {nb50} billet de 50€")
            elif montant >= 20:  # Pas de billets de 50€
                nb20 = math.floor(montant / 20)
                montant -= (20*nb20)
                if montant >= 10:
                    nb10 = 1
                    if nb20 > 1 and nb10 == 1:
                        return(f"Billets distribués:\n- {nb20} billets de 20€\n- {nb10} billet de 10€")
                    elif nb20 == 1 and nb10 == 1:
                        return(f"Billets distribués:\n- {nb20} billet de 20€\n- {nb10} billet de 10€")
                else:  # Que des billets de 20€
                    if nb20 > 1:
                        return(f"Billets distribués:\n- {nb20} billets de 20€")
                    else:
                        return(f"Billet distribué:\n- {nb20} billet de 20€")
            else:  # Qu'un billet de 10€
                nb10 = 1
                return(f"Billet distribué:\n- {nb10} billet de 10€")


montant = int(input("Entrez le montant à retirer : "))
verif = False
while verif == False:
    if verification(montant) == "Le montant doit être un multiple de 10 !":
        print("Le montant doit être un multiple de 10 !")
        montant = int(input("Entrez le montant à retirer : "))
    elif verification(montant) == "Le montant ne doit pas dépasser 500 (limite de retrait)":
        print("Le montant ne doit pas dépasser 500 (limite de retrait)")
        montant = int(input("Entrez le montant à retirer : "))
    else:
        verif = True
        print(verification(montant))
    