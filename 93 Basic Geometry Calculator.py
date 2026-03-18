import math
def calculate_rectangle_area(length, width):
    area = length * width
    return area
def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area
def main():
    choice = int(input("enter choice 1 to 2: "))
    if choice == 1:
        print(f"area of rectangle is {calculate_rectangle_area(5,8)}")
    elif choice == 2:
        print(f"area of circle is {calculate_circle_area(3)}")
    else:
        print("invalid choice")
main()