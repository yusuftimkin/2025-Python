print("Welcome Python Pizza!")

bill = 0

size = input("What size pizza do you want? S, M or L:\n")
peperoni = input("Do you want peperoni? Y or N:\n")
cheese = input("Do you want extra cheese? Y or N:\n")

if size == "S":
    if peperoni == "Y":
        bill += 17
    else:
        bill += 15
elif size == "M":
    if peperoni == "Y":
        bill += 23
    else:
        bill += 20
elif size == "L":
    if peperoni == "Y":
        bill += 28
    else:
        bill += 25
    
else:
    print("please enter a valid choice.")

if cheese == "Y":
    bill += 1

print(f"Your total bill is {bill} USD.")