height = float(input("Enter your height in m:"))
weight = float(input("Enter you weight in Kgs:"))
bmi= round(weight/height**2,1)
print("Your BMI is: "+str(bmi))
if bmi<18.5:
    print("You are underweight.")
elif bmi<25:
    print("You weight is normal.")
elif bmi<30:
    print("You are overweight.")
elif bmi<35:
    print("You are obese.")
else:
    print("You are clinically obese.")