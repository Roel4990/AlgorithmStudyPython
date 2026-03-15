import sys
input = sys.stdin.readline

weight = float(input())
height = float(input())

BMI = weight / (height * height)

if BMI > 25:
    print("Overweight")
elif BMI >= 18.5:
    print("Normal weight")
else:
    print("Underweight")
