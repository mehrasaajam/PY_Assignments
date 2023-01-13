
weight = float(input("please enter your weight (kg): "))
height = float(input("please enter your height (m): "))

BMI = weight/height**2

print("your BMI is equal to ", BMI)

if BMI < 18.5:
    print ("Therefore Your body mass index is underweight")

elif BMI >= 18.5 and BMI < 25:
    print("Therefore Your body mass index is normalweight")

elif BMI >= 25 and BMI < 30:
    print("Therefore Your body mass index is overweight")

elif BMI >= 30 and BMI < 35:
    print("Therefore Your body mass index is obesity")

elif BMI >= 35 and BMI < 40:
    print("Therefore Your body mass index is extreme obesity")

else:
    print("Therefore Your body mass index isnot in acceptable rang")
