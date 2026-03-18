print("Simple Interest Calculator")
principal = float(input("enter principal amount "))
rate = float(input("enter rate of interest "))
time_in_years = float(input("enter time in years: "))
simple_interest = (principal * rate * time_in_years) / 100

print(f"simple interest is {simple_interest}")