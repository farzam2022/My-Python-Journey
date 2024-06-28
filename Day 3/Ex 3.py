year = int(input("Enter year:"))
if year%4==0 & year%100!=0 & year%400!=0:
    print("This is not a Leap Year.")
else:
    print("This is a Leap Year.")