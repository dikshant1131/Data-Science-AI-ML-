# STRINGS IN PYTHON : 

# you can either use single quotation or double quotation for string

# print("hello")
# print('hello')

# to print : This is "Python" class

# print('This is "Python" class')

# to print : This is 'Python' class
# print("This is 'Python' class")

# to print : This is 'Python' "class"
# print("This is 'Python' \"class\"")

# -----------------------------------------------------------

# Multi line string: 

# a = """This 
# is
# multi line 
# string"""

# print(a)

# print("""Hello world
# Welcome to my Python Class""")

# a = "Hello world\nWelcome to my \nPython Class"
# print(a)

# a = "Hello world\tWelcome to my\tPython Class"
# print(a)

# ---------------------------------------------------------

# len() function : counts no. of letters including special symbols , numbers and space

# word = "Hello World!"
# print(len(word))

# ---------------------------------------------------------

# to check whether a word exist in string or not:

# sentence = "Hello world! Welcome to my Python class"

# print("Python" in sentence) # it return True or False

# ------------------------------------------------------------------

# INDEXING IN STRING : 

# word = "Hello World!"

# print(word[-5])
# print(word[4])

# ------------------------------------------------------------------

# SLICING OF STRING : 

word = "Hello World"

# print(word[5:9])
# print(word[-6:-2])
# print(word[-8:2])
# print(word[-7:-1])
# print(word[-1:-7])
# print(word[-7:])
# print(word[-7:0])
# print(word[:7])
# print(word[:])

# word = "Hello World"

# print(word[::3])
# print(word[::-1])
# print(word[-7:0:-2])

# ------------------------------------------------------------------

# MODIFICATION OF STRING : 

# word = "  harpreet kaur    "

# print(word.upper())
# print(word.lower())
# print(word.title())
# print(word.capitalize())
# print(word.strip())
# print(word)


# word = "hello worlod"
# print(word.split("o"))
# print(word.partition("o"))

# sentence = "Hello world! Welcome to Python Class"
# print(sentence.split(" "))

# word = "Hello world"

# print(word.replace("h","w"))

# print(word.isnumeric())

# a = "64657 "
# b="hello"
# c = "hello123"
# print(a.isnumeric())
# print(a.strip().isnumeric())

# print(a.isalpha())
# print(b.isalpha())

# print(a.isalnum())

# isupper, islower ,istitle


# a = "hello world"
# print(a.capitalize())

# ------------------------------------------------------------------

# concatination  :

# first_name = "Harpreet" 
# second_name = "Kaur"
# full_name = first_name +" "+ second_name
# print(full_name)

# print(5+3)
# print("5"+"3")

# ------------------------------------------------------------------

# input in python  : input()

# first_name = input("Enter your first name : ")
# second_name = input("Enter your last name : ")
# full_name = first_name +" "+ second_name
# print("Your full name is : " + full_name)

# ------------------------------------------------------------------

# Program to find sum of two numbers taking input from user side : 

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# addition = num1 + num2
# print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(addition))
# print(f"The sum of {num1} and {num2} is {addition}")

# output ---> The sum of 5 and 10 is 15
# num1 ---> 5 
# num2 ---> 10

