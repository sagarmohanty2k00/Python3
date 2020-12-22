# BMI Calculator
# bmi = weight(kg)/height^2(m^2)
# 
# 
# BMI chart
#   < 18.5 Under Weight
#   >18.5 and <25 Normal Weight
#   >25 and <30 Over Weight
#   >30 and <35 Obese
#   >35 Clinically Obese


weight = float(input("What is your weight(in KGs): "))
height = float(input("What is your height(in m):"))


bmi = round(weight/(height**2), 1)

if bmi>0 and bmi<18.5:
    print(f"Your BMI is {bmi}, you are slightly Underweight.")

if bmi>18.5 and bmi<25:
    print(f"Your BMI is {bmi}, you are Normal Weight.")

if bmi>25 and bmi<30:
    print(f"Your BMI is {bmi}, you are slightly Overweight.")

if bmi>30 and bmi<35:
    print(f"Your BMI is {bmi}, you are Obese.")

if bmi>35:
    print(f"Your BMI is {bmi}, you are Clinically Obese.")