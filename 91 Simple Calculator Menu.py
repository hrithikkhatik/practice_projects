# Simple Calculator Menu
while True:
    print("""
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
""")
    choice = int(input("enter choice from 1 to 5: "))
    if choice == 1 :
        number1 = int(input("enter number1: "))
        number2 = int(input("enter number2: "))
        print(f"sum of number1 and number2 is {number1+number2}")
    elif choice ==  2:
        number1 = int(input("enter number1: "))
        number2 = int(input("enter number2: "))
        print(f"subtract of number1 and number2 is {number1-number2}")
    elif choice == 3 :
        number1 = int(input("enter number1: "))
        number2 = int(input("enter number2: "))
        print(f"multiply of number1 and number2 is {number1*number2}")
    elif choice == 4 :
        number1 = int(input("enter number1: "))
        number2 = int(input("enter number2: "))
        if number2 != 0:
            print(f"divide of number1 and number2 is {number1/number2}")
        else:
            print("zero division error")
    elif choice == 5:
        print("goodbye")
    else:
        print("kindly choice 1 to 5")

