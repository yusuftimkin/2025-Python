print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12 or 15\n"))
people = int(input("How many people to split the bill?\n"))
split_bill = (bill * ( 1 + (tip / 100))) / people
split_bill = round(split_bill, 2)
print(f"Each person should pay: $ {split_bill}" )