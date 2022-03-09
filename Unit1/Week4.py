a = 5
b = 2
c = 3
print(a + b * c)

num = 99
num = 5
print(num)

'''
fave_food 
DECLARE String favouriteFood 
DISPLAY "What is the name of your favourite food?" 
INPUT favouriteFood 
DISPLAY "Your favourite food is " 
DISPLAY "favouriteFood" 
 '''
#favouriteFood = input("What is the name of your favourite food? ")
#print(f"Your favourite food is: {favouriteFood}")

'''
first_prize 
DECLARE String 1stPrize 
DISPLAY "Enter the award for first prize." 
INPUT 1stPrize 
DISPLAY "The first prize winner will receive ", 1stPrize 
 '''
#firstPrize = input("Enter the award for first prize: ")
#print(f"The first prize winner will receive: {firstPrize}")
'''
average_score 
DECLARE Integer lowest, highest, average 
DISPLAY "Enter the lowest score." 
INPUT lowest 
DISPLAY "Enter the highest score." 
INPUT highest 
SET average = low + high / 2 
DISPLAY "The average is ", average, "." 
'''
#lowest = 0
#highest = 0
#average = 0
#lowest = float(input("Enter the lowest score: "))
#highest = float(input("Enter the highest score: "))
#average = (lowest + highest) / 2
#print(f"The average is {average}")
'''
Room_length 
DISPLAY "Enter the length of the room." 
INPUT length 
DECLARE Integer length 
'''
#length = int(input("Enter the length of the room: "))
#print(f"The length of the room is: {length}")

print("Information Survey")
name = input("Whats your given name: ")
address = input("Whats your address (include city, state and postcode): ")
phone = input("Whats your telephone number: ")
job = input("Whats your dream future job: ")
print("")
print(f"My name is: {name}")
print(f"I live in: {address}")
print(f"Call my number @: {phone}")
print(f"I want to be: {job} when im older")
