montant = int(input("Entrez le montant total de vos achats : "))
remise = 0.9  # Remise de 10%
if montant > 100:
    total = round(montant * remise, 2)  # 2 chiffres aprés la virgule maximum
    print(f"Vous bénéficiez d'une remise de 10%. Montant à payer : {total}€")
else:
    print(f"Pas de remise. Montant à payer : {montant}")
