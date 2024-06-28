print("Welcome to Python Pizza!.")
size=input("What size Pizza do you want? S, M or L.")
add_pepperoni=input("Do you want pepperoni? Y or N.")
extra_cheese=input("Do you want  extra cheese? Y or N.")
total_price=0
if size=="S":
    if add_pepperoni=="Y":
        total_price=total_price+17
    else:
        total_price=total_price+15
elif size=="M":
    if add_pepperoni=="Y":
        total_price=total_price+23
    else:
        total_price=total_price+20
else:
    if add_pepperoni=="Y":
        total_price=total_price+28
    else:
        total_price=total_price+25
if extra_cheese=="Y":
    total_price=total_price+1
print("Total price: $"+str(total_price))