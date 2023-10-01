# main.py
import Lommeregner

# Bruger input
tal1 = float(input("Enter the first number: "))
tal2 = float(input("Enter the second number: "))

# Udfør kald til lommeregner modul
plus_resultat = lommeregner.plus(tal1, tal2)
minus_resultat = lommeregner.minus(tal1, tal2)
gange_resultat = lommeregner.gange(tal1, tal2)
divider_resultat = lommeregner.divider(tal1, tal2)

# Vis resultat
print("Plus: ", tal1, "+", tal2, "=", plus_resultat)
print("Minus: ", tal1, "-", tal2, "=", minus_resultat)
print("Gange: ",tal1, "* ",tal2, "=", gange_resultat)
print("Divider: ",tal1, "/", tal2, "=", divider_resultat)
