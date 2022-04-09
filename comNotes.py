# Commentaires de notes

try:
    note = int(input("Saisissez une note : "))
except ValueError:
    print("Vous devez saisir un nombre !")
   
if note < 10:
    print("Médiocre")
if note >= 10 and note <= 11:
    print("Passable")
if note >= 12 and note <= 13:
    print("Assez bien")
if note >= 14 and note <= 15:
    print("Bien")
if note >= 16 and note <= 17:
    print("Très bien")
if note >= 18:
    print("Excellent")
    
