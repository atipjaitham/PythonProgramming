# Loops

# for loop
fruits = ["apple", "orange", "pear", "cherry", "grape"]

# Use i for simple
for i in fruits:
    print("Would you like {} ?".format(i))

# Assign first and end number
for number in range(1,11):
    print("Number {}".format(number))

# While loop
temp_f = 40

# Loop controls "break"
while temp_f > 32:
    print("The weather is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f ==33:
        break

# Loop controls "continue"
for number in range(1,11):

    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}".format(number))

# Loop controls "pass"
for number in range(1,11):
    if number == 3:
        pass
    else: 
        print("The number is {}.".format(number))

# While loop in functions calculator
on = True

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

while on:
    operation = input("Please type +,-,*,/ or q : ")
    if operation == '+':
        add()
    elif operation == '-':
        subtraction()
    elif operation == '*':
        multiply()
    elif operation == "/" or "%":
        divide()
    elif operation == "q":
        on = False
    else:
        print("Please select type again!")