print("Welcome to the BMI calculator!")

weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in cm: "))

bmi = weight / ((height * 0.01) ** 2)

print(f"Your BMI index is {round(bmi,2)}")

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")