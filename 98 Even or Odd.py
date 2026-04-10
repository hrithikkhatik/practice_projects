number = int(input("enter a number: "))

if number == 0:
    print("Zero")
elif number % 2  == 0:
    print("even")
else:
    print("odd")

# Largest of 3 Numbers
number1 = float(input("enter a number1: "))
number2 = float(input("enter a number2: "))
number3 = float(input("enter a number3: "))

if number1 == number2 == number3:
    print("all number are equal")
elif number1 >= number2 and number1 >= number3:
    print("number1 is greater")
elif number2 >= number3 and number2 >= number1:
    print("number2 is greater")
else:
    print("number3 is greater")

# Marks → Grade
subject1 = float(input("enter marks of subject1"))
subject2 = float(input("enter marks of subject2"))
subject3 = float(input("enter marks of subject3"))

total = subject1 + subject2 + subject3
average = total / 3
if average >= 90:
    print("Grade is A")
elif average >= 75:
    print("Grade is B")
elif average >= 50:
    print("Grade is C")
else:
    print("fail")

# Leap Year

year = int(input("enter a year name to check leap year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("leap year")
else:
    print("not leap year")

# Simple Calculator
number1 = float(input("enter a number1: "))
number2 = float(input("enter a number2: "))

operator = input("enter operator like +,-,*,/: ")

if operator == "+":
    print(number1+number2)
elif operator == "-":
    print(number1-number2)
elif operator == "*":
    print(number1*number2)
elif operator == "/":
    if number2 == 0:
        print("zero division error")
    else:
        print(number1/number2)
else:
    print("enter valid operator")

# Number Type Checker
number = int(input("enter a number: "))

if number == 0:
    print("Zero")
elif number % 2 == 0 and number>0:
    print("positive even")
elif number % 2 != 0 and number >0:
    print("positive odd")
elif number % 2 == 0 and number<0:
    print("negative even")
elif number % 2 != 0 and number<0:
    print("negative odd")
