import random


a=input("Select 0 for Rock, 1 for Papers, 2 for Scissors")
comch= random.randint(0,2)
if a>=3 or a<0:
    print("You selected an invalid number you Lose!.")
elif comch==0 and a==2:
    print("You Lose!")
elif comch==2 and a==0:
    print("You win!")
elif comch>a:
    print("You Lose!")
elif a>comch:
    print("You Wins!")
elif comch==a:
    print("Draw!")