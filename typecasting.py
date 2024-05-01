a = "2" #here we have taken the value of a and b as strings
b = "5"
print(a+b) #this does not show the real result as they are strings

#EXPLICIT TYPECASTING

print(int(a)+int(b)) #using the int() function we can add the integer values even if it is a string

#IMPLICIT TYPECASTING

c = 2.4
d = 8
print(c+d) #here the result will automatically convert into float data type
print(type(c+d))