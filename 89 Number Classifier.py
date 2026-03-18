# Number Classifier
number = int(input("enter a number: "))
if number>0:
    print("The number is positive.")
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
elif number < 0:
    print("The number is negative")
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
elif number == 0:
    print("The number is zero")