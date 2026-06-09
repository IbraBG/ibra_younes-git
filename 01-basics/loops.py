
for i in range(10):
    print(i)

# range est pour passer une liste de nombre

for prenom in ["Emma","Clara","Malo","Ibrahim"]:
    print(f"Bonjour {prenom}")
    
    
total = 0

for i in range (1,11):
    total = total + i
    
print (total)


# while repete tant que la conditions est vrai 
age = 22

while age > 0 :
    if age < 18 :
        print (f"{age} - Mineur")
    elif age == 18 :
        print("Tu viens d'être majeur !")
    else:
        print(f"{age} - Majeur")
    age = age - 1