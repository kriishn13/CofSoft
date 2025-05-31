def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("Simple Calculator")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = input("Enter choice : ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", sub(num1, num2))
elif choice == '3':
    print("Result:", mul(num1, num2))
elif choice == '4':
    if num2 != 0:
        print("Result:", div(num1, num2))
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid input")
