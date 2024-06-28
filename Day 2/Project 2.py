print("Welcome to the tip Calculator")
tb=input("What was the total bill?")
per=input("What percentage tip would you like to give?10, 12, or 15?")
billtip= float(tb)*1.12
ppl=input("How many people to split the bill?")
billper=billtip/float(ppl)
print(round(billper,2))