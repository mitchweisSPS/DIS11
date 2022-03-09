#Checks for a number in a rang
def rangecheck(num): #this is called a function declaration
    #num = int(input("Enter a number: "))
    min = 0
    max = 100
    for i in range(min, max): #loop that continues for a known number iterations
        if num > min and num < max: #condition statement
            print(num)
            #exit()
            break
        else:
            print("Number is not in range")
            #exit()
            break
rangecheck(140)
rangecheck(20)
for i in range(50):
    a = i
    b = i * 10
    rangecheck(a)
    rangecheck(b)
    a += 1
    b -= 1
