# 1.	Write a program that asks user their height (cm) and weight (kg), and then calculate their BMI (Body Mass Index):
# BMI = mass (kg) / (height(m) x height(m) )
# Note: you must do the conversion from cm to m before calculation

# Then based on the BMI, tell them that they are:
# -	Severely underweight if BMI < 16
# -	Underweight if BMI is between 16 and 18.5
# -	Normal if BMI is between 18.5 and 25 
# -	Overweight if BMI is between 25 and 30
# -	Obese if BMI is more than 30

height_in_m = int(input("Please input your height in cm"))/ 100
weight_in_kg = int(input("Please input your weight in kg"))
BMI = weight_in_kg / (height_in_m ** 2)

if BMI < 16:
    print("Severely underweight")
elif 16<= BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25<= BMI < 30:
    print("Overweight")
else:
    print("Obese")

