def multiply(num1, num2):
    num3 = num1 * num2
    print(num3)
def divide(num1, num2):
    num3 = num1 / num2
    print(num3)
def add(num1, num2):
    num3 = num1 + num2
    print(num3)
def minus(num1, num2):
    num3 = num1 - num2
    print(num3)
def modulus(num1, num2):
    num3 = num1 % num2
    print(num3)
print("CALCULATOR")
function = (input("What function would you like to preform? (+,-,*,/,%): "))
num1 = int(input("Enter your first number you would like to use: "))
num2 = int(input("Enter the second number you would like to use: "))

if function == "*":
    multiply(num1, num2)
elif function == "/":
    if num1 == 0:
        print("Number cant be divided by zero")
        exit()
    elif num2 == 0:
        print("Number cant be divided by zero")
        exit()
    elif num1 != 0:
        divide(num1, num2)
    elif num2 != 0:
        divide(num1, num2)
elif function == "+":
    add(num1, num2)
elif function == "-":
    minus(num1, num2)
elif function == "%":
    modulus(num1, num2)
