print("Welcome to the rollercoaster!")
height = float(input("Please enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = float(input("Please enter your age: "))

    if age < 12:
        bill = 7
        print("Ticket costs is 7 USD.")
    elif age <=18:
        bill = 12
        print("Ticket costs 12 USD.")
    elif 45 <= age <= 55:
        print("Calm down buddy. Here is a free ride!")
    else:
        bill = 18
        print("Ticket costs is 18 USD.")
    
    wants_photo = input("Do you want a photo? Please enter y or n: ")

    if wants_photo == "y":
        bill += 3
    
    print(f"Please pay {bill} USD.")
else:
    print("You are too short for ride the rollercoaster")