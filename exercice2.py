nombres = []
for i in range(5):  # Boucle 5 fois
    nombres.append(int(input("Entrez un nombre : ")))
else:
    nombreMax = max(nombres)  # Retourne le plus grand nombre de "nombres"
    print(f"Le plus grand nombres est {nombreMax}")