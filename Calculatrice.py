nombre_a_gauche = input("Entrez un nombre : ")
nombre_a_droite = input("Entrez un nombre : ")
operation = input("Entrez un symbole d'opération (+, -, * ou /) : ")
resultat = 0

if not (nombre_a_gauche.isnumeric()) or not (nombre_a_droite.isnumeric()):
  print("Erreur: les deux nombres doivent être des nombres entiers")
else:
  nombre_a_gauche = int(nombre_a_gauche)
  nombre_a_droite = int(nombre_a_droite)
  if operation not in ('+', '-', '*', '/'):
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'")
  else:
    if operation == '+':
        resultat = nombre_a_gauche + nombre_a_droite
    elif operation == '-':
        resultat = nombre_a_gauche - nombre_a_droite
    elif operation == '*':
        resultat = nombre_a_gauche * nombre_a_droite
    elif operation == '/':
        if nombre_a_droite == 0:
            print("Erreur: impossible de diviser par zéro.")
        else:
            resultat = nombre_a_gauche / nombre_a_droite

    print(f"Le résultat est : {resultat}")
