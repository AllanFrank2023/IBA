# Velkomst
print("Velkommen til lommeregneren!")

while True:
    # Valgmulighederne
    print("Vælg en regnemetode:")
    print("1. Addition, 2. Subtraktion, 3. Multiplikation, 4. Division")


    # Input brugerens valg
    valg = input("Indtast dit valg (1/2/3/4): ")

    # Afslut programmet ved valg udenfor 1-4
    if valg > '4':
        print("Ugyldigt valg. Prøv igen.")
        break

    # Indtast to tal
    tal1 = int(input("Indtast det første tal: "))
    tal2 = int(input("Indtast det andet tal: "))
    if tal1 > 15 and tal2 > 15:
        print("over 4 bits")

    # Udfør og viser resultatet
    if valg == '1':
        resultat = tal1 + tal2
        print("Resultatet er:", resultat)
    elif valg == '2':
        resultat = tal1 - tal2
        print("Resultatet er:", resultat)
    elif valg == '3':
        resultat = tal1 * tal2
        print("Resultatet er:", resultat)
    elif valg == '4':
        # Undgå division med nul
        if tal2 == 0:
            print("Kan ikke dividere med nul.")
        else:
            resultat = tal1 / tal2
            print("Resultatet er:", resultat)
    else:
        print("Ugyldigt valg. Prøv igen.")

print("Farvel og tak")