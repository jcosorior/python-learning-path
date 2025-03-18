import math
print("Welcome to oso_calculator.py ")
num1 = float((input(" type the first number you want to operate:")))
operation = (input("Wich operation you want to do?"))
num2 = float((input("type the second number you want to operate:")))




if operation == "+":
    result =num1 + num2 
    print(round(result, 2))
elif operation == "-":
    result =num1 - num2
    print(round(result, 2))
elif operation == "*":
    result =num1 * num2
    print(round(result, 2))
elif operation == "/":
    result =num1 / num2
    print(round(result, 2))
else:
    print(f"{operation} is not valid")

