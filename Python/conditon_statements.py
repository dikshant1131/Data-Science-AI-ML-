# if-else:

# SYNTAX : 

# if conditon :
        # statement1
        # statement2
        # statement3
        # statement4 .....
# elif condition : 
        # statement1
        # statement2
        # statement3
        # statement4 .....
# elif condition : 
        # statement1
        # statement2
        # statement3
        # statement4 .....
# else : 
        # statement1
        # statement2
        # statement3 .....

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# if num1>num2 : 
#     print(f"{num1} is greater")
# elif num1 == num2 :
#     print(f"Both numbers are equal")
# else:
#     print(f"{num2} is greater")

# ---------------------------------------------------------------------

# Program to check whether the number is even or odd taking number as input

# num = int(input("Enter any number : "))

# if num%2 == 0 :
#     print("Even number")
# else : 
#     print("Odd number")

# ---------------------------------------------------------------------

# Program to check whether the number/word is palindrome or not

# LEVEL ---> LEVEL
# MOM ---> MOM
# 12321 ---> 12321
# Level ---> leveL

# Harpreet ---> teerpraH
# 12345 ----> 54321

# word = input("Enter any word/number : ").strip()

# if word.lower() == word[ : :-1].lower():
#     print(f"{word} is Palindrome")
# else : 
#     print(f"{word} is not a Palindrome")

# a = 10

# if a==10:
#     print("a is 10")
# elif a==10:
#     print("ELIF STATEMENT")
# else :
#     print("a is not 10")

# ----------------------------------------------------------------

# Program to print grade of a student by taking marks of 4 subjects
# calculate percentage according to marks : 
# if percentage is higher than 90 ---> Grade A
# if percentage is between 70 and 90 ---> Grade B
# if percentage is between 50 and 70 ---> Grade C
# if percentage is between 35 and 50 ---> Grade D
# else ----> FAIL

# sub1 = int(input("English marks : "))
# sub2 = int(input("Mathamatics marks : "))
# sub3 = int(input("Science marks : "))
# sub4 = int(input("Geography marks : "))

# obtained_marks = sub1 + sub2 + sub3 + sub4
# total = 400
# percentage = (obtained_marks/total)*100

# print(percentage)

# if percentage >=90:
#     print("Grade A")
# elif percentage >= 70:
#     print("Grade B")
# elif percentage >= 50 :
#     print("Grade C")
# elif percentage >= 35 :
#     print("Grade D")
# else : 
#     print("FAIL")

# --------------------------------------------------------------------

# Program to find greatest among 3 numbers : 

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter third number : "))

# if num1 > num2 and num1 > num3 :
#     print(f"{num1} is greatest")
# elif num2 > num1  and num2 > num3 :
#     print(f"{num2} is greatest")
# else : 
#     print(f"{num3} is greatest")

# --------------------------------------------------------------------

# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria : 
# 
# >100000   -----> 15 %
# >50000 and <=100000 ----> 10 %
# <50000 ----> 5%

# 15% of cost ---> (15/100) * cost

# cost = int(input("Enter cost price of your bike : "))

# if cost > 100000 :
#     tax = (15/100) * cost
# elif cost > 50000:
#     tax = (10/100) * cost
# else :
#     tax = (5/100) * cost

# print(f"You have to pay {tax} raod tax\nYou have to pay total amount of {cost + tax}")

# ------------------------------------------------------------------

# name = input("Enter your name : ")
# bp = int(input("Enter your BP : "))

# calculating other variables :

# pf = (12/100) * bp

# hra = (20/100) * bp
# if hra > 2000:
#     hra = 2000

# if bp<300000 :
#     da = (20/100) * bp
# else : 
#     da = (30/100) * bp

# grosspay = bp + da +hra - pf
# netpay = grosspay - pf

# print(f"Your grosspay would be {grosspay} and netpay is {netpay}")

# ------------------------------------------------------------------

# NESTED IF-ELSE : 

# password = input("Enter your password : ")

# if password == "Harpreet098" :
#     print("You are logged in!")
# else : 
#     print("Incorrect Password")
#     password = input("Enter your password again : ")
#     if password == "Harpreet098":
#         print("You are logged in!")
#     else :
#         print("Incorrect password again!")

# ------------------------------------------------------------------
# 250 ---> 100 * 0 + 100 *5 + 50 *10

# units = int(input("Enter number of units : "))

# if units <= 100 :
#     bill = 0
# elif units <= 200:
#     bill = (units-100) * 5
# else : 
#     bill = 500 + (units - 200) * 10

# print(f"You have to pay {bill} for {units} units")

# ------------------------------------------------------------------

# program to find the greatest of three numbers (taking input from user) without using logic operators (using nested if-else statements)

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = int(input("Enter third number : "))

# if num1 > num2 : 
#     if num1 > num3 :
#         print(f"{num1} is greatest")
#     else :
#         print(f"{num3} is greatest")
# else : 
#     if num2 > num3 :
#         print(f"{num2} is greatest")
#     else :
#         print(f"{num3} is greatest")


# ------------------------------------------------------------------

# Leap year : 

year = int(input("Enter a year : "))

if (year%4==0 and year%100 != 0) or (year%400)==0 :
    print("Leap Year")
else : 
    print("Not a Leap Year")


