password = input("Entrez un mot de passe : ")

def verif_password(password):
    nombres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(password) >= 8:
        password_tab = list(password)
        # T'as dit que tu voulais pas de boucle, je vois pas l'interêt mais VOILA 
        if nombres[0] in password_tab or nombres[1] in password_tab or nombres[2] in password_tab or nombres[3] in password_tab or nombres[4] in password_tab or nombres[5] in password_tab or nombres[6] in password_tab or nombres[7] in password_tab or nombres[8] in password_tab or nombres[9] in password_tab:
            return("Mot de passe valide")
        else:
            return("Mot de passe invalide (doit contenir au moins un chiffre)")
    else:
        return("Mot de passe invalide, (doit contenit au moins 8 caractères dont un chiffre)")

# Sinon la fonction avec boucle
# def verif_password(password):
#     nombres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     if len(password) >= 8:
#         for caractere in password:
#             if caractere in nombres:
#                 return("Mot de passe valide")
#         else:
#             return("Mot de passe invalide (doit contenir au moins un chiffre)")
#     else:
#         return("Mot de passe invalide, (doit contenit au moins 8 caractères dont un chiffre)")

print(verif_password(password))