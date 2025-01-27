# For Loop:

# print hello world 20 times : 

# for i in range(5):
#     print("Hello World")

# for i in range(5):
#     print(i)

# for i in range(5,10):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# ------------------------------------------------------------------
# PROGRAM TO PRINT EVEN NUMBERS BETWEEN 1 AND 20  :

# for i in range(2,21,2):
#     print(i)

# for i in range(1,21):
#     if i%2==0:
#         print(i)

# ---------------------------------------------------------------------
# PROGRAM TO PRINT EVEN NUMBERS BETWEEN A RANGE TAKING INPUT FROM USER

# start = int(input("Enter starting range : "))
# end = int(input("Enter ending range value : "))

# for i in range(start,end+1):
#     if i%2==0:
#         print(i)

# ---------------------------------------------------------------------

# for loop in list : 

# fruits = [ "apple","mango","banana","guava","kiwi","cherry","strawberry","black berry"]

# sum = 0
# for i in fruits:
#     sum += 1

# print(sum)

# ---------------------------------------------------------------------
# Program to calculate sum of all the numbers in the given list:

# numbers = [53,75,42,67,48,58,10,22,1,65]

# total = 0
# for num in numbers:
#     total += num

# print(total)

# ---------------------------------------------------------------------

# FOR LOOP IN STRING : 

# sentence = "Hello world"

# for char in sentence:
#     print(char)

# ---------------------------------------------------------------------

# Program to calculate total number of vowels in a string:

# sentence = "Hello world. Welcome to Chandigarh"

# vowel_count = 0
# for char in sentence:
#     if char.lower() in "aeiou":
#         vowel_count +=1

# print(vowel_count)

# ---------------------------------------------------------------------

# Program to calculate total number of vowels and consonents in a string:

# sentence = "Hello world. Welcome to Chandigarh"
# vowels_count = 0
# consonent_count = 0

# for i in sentence:
#     if i.isalpha():
#         if i.lower() in "aeiou":
#             vowels_count+=1
#         else:
#             consonent_count+=1

# print(f'Number of vowels in given sentence are {vowels_count}')
# print(f'Number of consonent in given sentence are {consonent_count}')

# ---------------------------------------------------------------------

# Count numbers and alphabets in a string : 

# sentence = "H34ello 234 world 23 @how are you 1!"

# ---------------------------------------------------------------------

# Count fruit in which "e" occurs from the following list : 

# fruits = [ "apple","mango","banana","guava","kiwi","cherry","strawberry","black berry"]
# count = 0

# for i in fruits :
#     if "e" in i:
#         count+=1

# print(count)

# ---------------------------------------------------------------------

# Program to swap first and last element in a list : 

# fruits = [ "apple","mango","banana","guava","kiwi","cherry","strawberry","black berry"]

# fruits[0],fruits[-1] = fruits[-1],fruits[0]
# print(fruits)

# ---------------------------------------------------------------------

# Program to remove duplicate elements in a list
# list1 = [4,2,5,2,5,7,23,57,3,5,2]
# list2 = []

# for i in list1:
#     if i not in list2:
#         list2.append(i)

# print(list2)

# ---------------------------------------------------------------------

# Given two lists, find the common elements without using loop:

list1 = [3,5,2,6,4,78]
list2 = [3,78,0,34,1,45]

# ---------------------------------------------------------------------

# FOR LOOP IN TUPLE : 

# tuple1 = (36,24,85,35,86)

# for i in tuple1:
#     print(i)

# ---------------------------------------------------------------------

# FOR LOOP IN SET:

# set1 = {3,782,46,25,72,3,46}

# for i in set1:
#     print(i)

# ---------------------------------------------------------------------

# FOR LOOP IN DICTIONARY : 

# student_detail = {
#     "name" : "Harpreet Kaur",
#     "Course" : "B.tech",
#     "Age" : 22,
#     "email" : "harpreet@gmail.com" }

# print(student_detail["Age"])
# for i in student_detail:
#     print(i)

# print(student_detail.values())

# for i in student_detail.values():
#     print(i)

# for key,value in student_detail.items():
#     print(f"{key} = {value}")

# for i in student_detail:
#     print(f"{i} = {student_detail[i]}")


# ---------------------------------------------------------------------

# BREAK :

# for i in range(10):
#     print(i)
#     if i == 6:
#         break

# ---------------------------------------------------------------------

# CONTINUE : 

# for i in range(10):
#     if i== 6 :
#         continue
#     print(i)

# print even numbers between 1 and 20 using continue :

# for i in range(1,21):
#     if i%2 !=0:
#         continue
#     print(i)

# ---------------------------------------------------------------------

# To check whether the number(taking number as input) is prime or not 

# num = int(input("Enter any number : "))

# prime = True

# for i in range(2,num**0.5):
#     if num% i == 0:
#         prime = False
#         break

# if prime:
#     print(f"{num} is a Prime number")
# else :
#     print(f"{num} is not a Prime number")


# 16 ----> 4*4
# 25 -----> 5 * 5
# 10 ----> 2*5 

# ---------------------------------------------------------------------
# Program to count occurance of each character in a string : 

# string = input("Enter a string : ")
# char_count = {}

# for i in string.lower():
#     if i in char_count:
#         char_count[i] +=1
#     else:
#         char_count[i] = 1

# print(char_count)

# ---------------------------------------------------------------------

# fabonacci series : 

# 0 1 1 2 3 5 8 13 21......

# n1 = 0
# n2 = 1

# terms = int(input("Enter number of terms : "))

# if terms ==1 :
#     print(n1)
# elif terms == 2 :
#     print(n1)
#     print(n2)
# else : 
#     print(n1,n2,end=" ")
#     for i in range(terms - 2):
#         n3 = n1+ n2
#         print(n3,end=" ")
#         n1 = n2
#         n2 = n3

# fabonacci series in a list : 
# [0,1,1,2,3,5]
# terms = int(input("Enter number of terms :"))

# fibb =  [0,1]
# for i in range(terms-2):
#     next_term =  fibb[-2] + fibb[-1]
#     fibb.append(next_term)

# print(fibb)

# ---------------------------------------------------------------------

# to check whether the number is armstrong or not

# 153 ---> 1 ** 3  +  5  **  3 +  3  ** 3 ----> 1 + 125 + 27 ---> 153

# num = input("Enter any number : ")

# def armstrong(num):
#     num = str(num)
#     length = len(num)
#     add = 0

#     for i in num:
#         add += int(i) ** length

#     if add == int(num) :
#         return True
#     else : 
#         return False

# if armstrong(num):
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# num = int(input("Enter a number : "))
# length = len(str(num))
# temp = num
# add= 0
# for i in range(length):
#     digit = temp%10
#     add += digit ** length
#     temp //= 10
# if add == num :
#     print("Armstrong number")
# else : 
#     print("Not an Armstrong number")

# ---------------------------------------------------------------------

# program to print factorial of a number
# 5 --->  5*4*3*2*1    ---> 1*2*3*4*5
# 7 --->  7*6*5*4*3*2*1  ----> 1*2*3*4*5*6*7

# num = int(input("Enter a number : "))
# if num<0:
#     print("Negative numbers have no factorial")
# elif num==0 or num==1 :
#     print(f"Factorial of {num} is 1")
# else :
#     fac = 1 
#     for i in range(2,num+1):
#         fac *= i
#     print(f"Factorial of {num} is {fac}")

# ---------------------------------------------------------------------

# Patterns : 

# 1) square pattern

# # # #
# # # #
# # # #
# # # #

# sides  = int(input("Enter side of square : "))
# for i in range(sides):
#     print("# " * sides)

# 2) right triangle : 

#                         i = 0
# #                       i = 1
# # #                     i = 2
# # # #                   i = 3
# # # # #                 i = 4

# height  = int(input("Enter height of triangle : "))
# for i in range(height):
#     print("# " * (i+1))

# height  = int(input("Enter height of triangle : "))
# for i in range(1,height+1):
#     print("# " * (i))

# fabonacci series :

# 0 1 1 2 3 5 8 13 .....
# [0,1,1,2,3,5,8]

# n = int(input("Enter number of terms : "))
# fabb = [0,1]

# for i in range(n-2):
#     next_no = fabb[-2] + fabb[-1]
#     fabb.append(next_no)

# terms = int(input("Enter number of terms : "))
# n1 = 0
# n2 = 1

# if terms == 1 : 
#     print(n1)
# elif terms == 2 :
#     print(n1,n2)
# else :
#     print(n1,n2,end=" ")
#     for i in range(terms-2):
#         n3 = n1 + n2
#         print(n3,end=" ")
#         n1 = n2
#         n2 = n3


# print("hello "*5)
# a = "5"*3
# print(a)

# pattern :

# square pattern : 

# # # #
# # # #
# # # #
# # # #

# side = int(input("Enter side of square : "))
# for i in range(side):
#     print("# "*side)

#                     i = 0
# #                   i = 1
# # #                 i = 2
# # # #
# # # # # 
# height = int(input("Enter height of right angle triangle : "))
# for i in range(height):
#     print("# "* (i+1))

