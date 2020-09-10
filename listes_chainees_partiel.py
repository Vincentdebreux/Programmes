tab = [None, None]

def ajouter(tab, element):
	suivant = tab #On lui donne la valeur de la liste
	if tab[0] == None:
		suivant[0] = element
	else:
		while suivant[1] != None: #On incrémente i jusqu'a qu'on trouve le "None" du dernier tableau
			suivant = suivant[1] #A chaque fois on prend le tableau suivant
		suivant[1] = [element, None] #Et donc on crée le nouveau tableau avec la valeur à la place de "None"

def inserer(tab, index, element):
    suivant = tab #On lui donne la valeur de la liste
    for _ in range(index-1): #On refait l'opération jusqu'à l'index voulu
        suivant = suivant[1] #A chaque fois on prend le tableau suivant
    suivant[1] = [element, suivant[1]] #On redéfinis la valeur à celle donné

def acceder(tab, index):
    suivant = tab #On lui donne la valeur de la liste
    for _ in range(index): #On refait l'opération jusqu'à l'index voulu
        suivant = suivant[1] #A chaque fois on prend le tableau suivant
    print(suivant[0]) #On affiche la valeur

def longueur(tab):
    suivant = tab #On lui donne la valeur de la liste
    i = 0 #Correspondra à la taille
    if tab[0] == None: #Si la liste est vide
        return i
    while suivant[1] != None: #On incrémente i jusqu'a qu'on trouve le "None" de la dernière valeur
        i += 1
        suivant = suivant[1] #A chaque fois on prend le tableau suivant
    return i+1 #On ajoute 1 car il y a une valeur en trop

def supprimer_ind(tab, index):
	suivant = tab #On lui donne la valeur de la liste
	if index == 0:
		suivant[0] = suivant[1][0]
		suivant[1] = suivant[1][1]
	else:
		for _ in range(index-1): #On continue jusqu'à l'index-1 donné pour avoir le tableau juste avant celui de l'index
			suivant = suivant[1] #A chaque fois on prend le tableau suivant
		suivant[1] = suivant[1][1] #Et donc remet à l'ancienne valeur la suite de la liste

def supprimer_val(tab, valeur):
    ancien = None
    suivant = tab #On lui donne la valeur de la liste
    while suivant[0] != valeur: #tant que la valeur de suivant[0] n'est pas égale à la valeur demandée,
        ancien = suivant #on sauvegarde suivant
        suivant = suivant[1] #et on avance dans la liste
    if ancien == None: #si ancien est vide, alors on supprime la premiève valeur
        suivant[0] = suivant[1][0]
        suivant[1] = suivant[1][1]
    else:
        ancien[1] = suivant[1] #sinon, on remplace ancien par suivant[1]

def modifier(tab, index, value):
    suivant = tab #On lui donne la valeur de la liste
    for _ in range(index): #On continue jusqu'à l'index donné
        suivant = suivant[1] #A chaque fois on prend le tableau suivant
    suivant[0] = value #Et donc on donne à l'index donné, la valeur donné

def vider(tab):
    tab = [None, None] #Je remet les valeurs initiales

ajouter(tab,5)
ajouter(tab,2)
ajouter(tab,4)
ajouter(tab, 9)
print(tab)
supprimer_val(tab,4)
print(tab)
