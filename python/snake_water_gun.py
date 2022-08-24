import random

def gamew(comp, you):

    if comp == you:
        return None

    elif comp == 's':
        if you == 'w':
            return False

        elif you == 'g':
            return True

    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer Turn: Choose between Snake(s), Water(w) or Gun(g)")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'

elif randNo == 2:
    comp = 'w'

elif randNo == '3':
    comp = 'g'

you = input('''your's turn: 
Choose between Snake(s), Gun (g) or Water(w): ''')

print(f"computer choose: ", comp)

a = gamew(comp, you)
if a == None:
    print("The game is tie!!!")

elif a == True:
    print("You Won!!!")

else:
    print("you loose!!!")