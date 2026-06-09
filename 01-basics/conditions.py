



# True ou False opérateur ( <,>,>=,<=,!=)



age = int(input("Quelle âge as-tu ? :"))

if age == 18:
    print(f"Tu as {age} et tu viens juste d'être majeur")
elif age > 18:
    print("Tu as {age} et tu est un adulte")
elif age < 18:
    print("tu as {age} et tu est un adolescent")
elif age > 65:
    print ("Tu as {age} et tu est un senior")
else:
    print("la boonne nouvelle c'est que tu as {age} et tu n'est pas pris en compte sorry !")
    
    
if age % 2 == 0 :
    print("Ton âge est un nombre  paire")
else:
    print("Ton âge es un nombre impaire")
    
#combiner condition ( and ( les deux condition odivent etre vrais) , or ( au moins l'une des deux doit etre vrai), not (n'est pas) )1