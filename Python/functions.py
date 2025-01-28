# User defined functions : 

# 1) Non-parametrized functions :

# syntax : 

# declaring a function:
# def function_name():
#           statements

# calling a function : 
# function_name()

# def hello():
#     print("Hello world")
#     print("Welcome to CHD")

# hello()
# hello()

# def hello():
#     return """Hello world
# Welcome to CHD"""

# print(hello())

# num = 4
# def square():
#     print(4**2)

# num = square() + 4
# print(num)

# num = 4
# def square():
#     return num **2

# num1 = square() + 4
# print(num1)

# 2) parametrized functions : 

# def square(num):
#     return num **2

# print(square(5))

# def add(num1, num2):
#     return num1+ num2

# print(add(9,7))

# x = int(input("Enter first number : "))
# y = int(input("Enter second number : "))
# print(add(x,y))


# def square_pattern(sides):
#     for i in range(sides):
#         print("# " * sides)

# square_pattern(4)

# LAMBDA FUNCTION : 
# it is a function without name 
# or you can say it is a anonymous function 

# x = lambda l,b : 2*(l+b)

# print(x(10,5))


# decorators : 

# decorator is a function that takes function as an argument
# and return a modified function
# adds extra functionality to existing function

def decorate(func):
    def modified_func():
        print("Good morning")
        func()
        print("Thank you")
    return modified_func

@decorate
def hello():
    print("Hello world")

hello()
# decorate(hello)