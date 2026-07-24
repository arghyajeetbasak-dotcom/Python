def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Division by zero"

while True:
    print("\n--- Simple Calculator ---")
    print(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Exit")

    choice=input("Enter your choice(1-5) : ")
    if(choice=='5'):
        print("Exiting calculator.")
        break
    elif(choice=='1' or choice=='2' or choice=='3' or choice=='4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Try again.")