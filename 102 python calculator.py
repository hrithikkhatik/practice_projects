num1 = float(input("enter a num1: "))
num2 = float(input("enter a num2: "))
operation = input("enter a character operation: ")

if -10 ** 9 <= num1 <= 10 ** 9  and -10 ** 9 <= num2 <= 10 ** 9:
    if operation == "+":
        print(f"sum {num1+num2}")
    elif operation == "-":
        print(f"subtraction {num1-num2}")
    elif operation == "*":
        print(f"multiplication {num1*num2}")
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(f"division {num1/num2}")
    else:
        print("Invalid operation")
else:
    print("enter valid number")