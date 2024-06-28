import random

names= input("Enter Everybody's name separated by a coma.")
op=names.split(", ")
num_items=len(op)
randc =random.randint(0,num_items-1)
print(op[randc])