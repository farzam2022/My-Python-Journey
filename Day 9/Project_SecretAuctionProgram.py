import os
print("Welcome to the Auction Program.")
b=True
bid_dictionary={}
while b==True:
    bid_dictionary[input("Enter Your name:")]= str(input("Enter your bid:"))
    if input("Are there any other users who want to bid? type 'yes' or 'no'")=="no":
        b=False
    else:
        def clear (): os.system ('cls')
max= 0
for key in bid_dictionary:
    if int(bid_dictionary[key])>int(max):
        max=int(bid_dictionary[key])
print(max)