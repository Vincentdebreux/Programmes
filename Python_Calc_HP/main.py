from Pile import *
pile = Pile()

while True:
    print('')
    print(pile)
    print('')
    resultat = 0
    prop = input('')
    try:
        prop = int(prop)
        pile.empiler(prop)
    except:
        if prop == 'q':
           break
        elif prop == '+':
            if len(pile) <= 1:
                print(pile.valeur[0])
                pile.empiler(pile.valeur[0])
                continue
            else:
                resultat = pile.valeur[0] + pile.valeur[1]
                print(resultat)
                pile.empiler(resultat)
                continue
        elif  prop == '-':
            if len(pile) <= 1:
                print("Erreur: Il n'y pas ou qu'une valeur dans la calculatrice")
                continue
            else:
                resultat = pile.valeur[0] - pile.valeur[1]
                print(resultat)
                pile.empiler(resultat)            
        elif prop == '*':
            pass
        elif prop == '/':
            pass
        elif prop == '**':
            pass
        elif prop == 'sin':
            pass
        elif prop == 'cos':
            pass
        elif prop == 'tan':
            pass
        elif prop == 'exp':
            pass
        elif prop == 'log':
            pass
        elif prop == 'log10':
            pass