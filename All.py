# Question 1 Task 1: Code Correction
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Question 2 Task 1: Identify The Greatest
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if(num1 > num2 and num1 > num3):
    print("First number is largest")
elif(num2 > num1 and num2 > num3):
    print("Second number is largest")
else:
    print("Third number is largest")

# Question 2 Task 2: Identify The Smallest
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if(num1 < num2 and num1 < num3):
    print("First is the smallest")
elif(num2 < num1 and num2 < num3):
    print("Second is smallest number")
else:
    print("Third number is the smallest number")

# Question 2 Task 3: Equality Check

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if(num1 == num2 and num1 > num3):
    print("First and Second numbers are equal and the largest")
elif(num1 == num3 and num1 > num2):
    print("First and Third numbers are equal and the largest")
else:
    (num2 == num3 and num2 > num1)
    print("Second and Thir numbers are equal and the largest")


num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if(num1 == num2 == num3):
    print("All numbers are equal")

# Question 3 Task 1: Leap Year Checker
year = int(input("Enter a year:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, "is a leap year:")
else:
    print(year, "is not a leap year!")