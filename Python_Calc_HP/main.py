from Pile import *
pile = Pile()

while True:
    prop = input(Proposition)
    if prop == 'q':
        break
    if int(prop) == True:
        pile.empiler(prop)