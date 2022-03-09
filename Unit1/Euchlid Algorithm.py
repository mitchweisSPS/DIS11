# Euchilds Algorithm
# Take 2 numbers
# Divide second into first
# Take remainder and divide into previous divisor
# eg 60 and 8
# 60/8 = 7 r 4; 8/4 = 2
# so GCD of 60 and 8 is 4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = None

while c != 0:
    c = a % b
    a = b
    b = c

print(a)
