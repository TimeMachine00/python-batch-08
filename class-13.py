# BMI calculator
height=float(input("enter your height\n"))

weight=float(input("enter your weight\n"))

BMI = round(weight/height**2, 2)

if BMI<18.5:
    print(f"your BMI is {BMI}, under weight")
elif BMI<25:
    print(f"your BMI is {BMI}, your Bmi is good")
elif BMI<30:
    print(f"your BMI is {BMI}, your obese")
else:
    print(f"your BMI is{BMI}, your clinically obese")
