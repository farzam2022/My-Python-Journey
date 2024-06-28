print("Welcome to Treasure Island")
if input("Do you want to go Left or Right? L or R.")=="R":
    print("You've Lost!")
else:
    if input("Do you want to Swim or Wait? S or W.")=="S":
        print("You've Lost!")
    else:
        c=input("Which door Red, BLue or Yellow? R, B or Y.")
        if (c=="R")|(c=="B"):
            print("You've Lost!")
        else:
            print("You Win!")