

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operator(+,-,*,/): ")

match c:
    case '+':
        print("The answer is", a + b)
    case '-':
        print("The answer is", a - b)     #match cases are basically the same as if else but may be more convinient in some situations32
    case '*':
        print("The answer is", a*b)
    case '/':
        if c == 0:
            print("Number cannot be divided by zero")
        else:
            print("The answer is", a / b)
            w