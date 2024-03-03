# Conditionals
print(1>1)
print(1<1)
print(1!=1)
print(1==1)
print(1>=1)
print(1<=1)

# If Statement
name = input("What's your name?")
if name == "Greg":
    print("Hello, nice to see you {}".format(name))
elif name == "John":
    print("Hello, {} welcome to system.".format(name))
elif name == "Andy":
    print("Hello, {} How are you? ".format(name))
else :
    print ("You don't have a permittion")
print("Have a nice day")

def add():
    a = float(input("Enter a number : "))
    b = float(input("Enter another number : "))
    print (a + b)

def subtraction():
    a = float(input("Enter a number : "))
    b = float(input("Enter another number : "))
    print (a - b)

def multiply():
    a = float(input("Enter a number : "))
    b = float(input("Enter another number : "))
    print (a * b)

def divide():
    a = float(input("Enter a number : "))
    b = float(input("Enter another number : "))
    print (a / b)

operation = input("Please type +,-,* or / ")
if operation == '+':
    add()
elif operation == '-':
    subtraction()
elif operation == '*':
    multiply()
elif operation == "/" or "%":
    divide()
else:
    print("Please select type again!")
