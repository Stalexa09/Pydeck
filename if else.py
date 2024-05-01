a = int(input("Enter you age: "))
print("You are is: ", a)

if (a < 18):  #if this is true
    print("You cannot drive.") #then this works
else:  #if that was not true
    print("You can drive") #this works


#conditional operators: <, >, <=, >=, ==, != (not equal to is ! = without the space)

print(a>=18) #prints in boolean 
print(a<=18)
print(a==18)
print(a!=18)
print(a>18)


budget = input("Enter you budget: ")
price = input("Enter the price: ")

if (budget >= price):
    print("You can buy the item")
else:
    print("You cannot buy this item")

#Elif

x = 195
y = 201

if (x >= y):          #if this is not true
    print("ok")
elif( y - x < 5):  #it will move to check if this is true
    print("Barely ok") #you can add as many elif's as you want
else:
    print("no")

#NESTED

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):            #You can put if statements inside other if statements
     
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")