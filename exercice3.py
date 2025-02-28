password = input("Entrez un mot de passe : ")

def verif_password(password):
    nombres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(password) >= 8:
        for caractere in password:
            if caractere in nombres:
                return("Mot de passe valide")
        else:
            return("Mot de passe invalide (doit contenir au moins un chiffre)")
    else:
        return("Mot de passe invalide, (doit contenit au moins 8 caractères dont un chiffre)")

print(verif_password(password))