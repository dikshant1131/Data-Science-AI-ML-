# TUPLES : 

# used to store multiple elements in single vaiable
# tuples are created using round brackers ()
# tuples are ordered
# tuple's elements can be of any datatype
# len() function is used to count number of elements in tuple
# type() is used to determine its data type
# tuple allow duplicacy

# tuples are unchangeable
# it takes less space in memory as compare to list
# tuples are fast as compared to list

mytuple = (1,2,3,4,5,6,1,1)
# print(mytuple)

# print(type(mytuple))
# print(len(mytuple))
# print(mytuple[2:5])

# mytuple[0]=100
# print(mytuple)

# mylist = list(mytuple)
# print(mylist)
# mylist[0] = 100
# mytuple = tuple(mylist)
# print(mytuple)

# ------------------------------------------------------------------

# UNPACKING A TUPLE :

# fruits = ("apple","mango","kiwi")
# red, yellow , brown = fruits

# print(red)
# print(yellow)
# print(brown)

# numbers = (53,64,24,785,534,85,43,85,345)

# x1 , x2 , *x3  = numbers

# print(x1)
# print(x2)
# print(x3)

# -------------------------------------------------------------

# Joining a tuple : 

# tuple1 = (1,2,3,4,5)
# tuple2 = (1,3,5,7,9)
# tuple3 = tuple2 + tuple1

# tuple1 = (1,2,3)
# tuple2 = tuple1 * 3

# print(tuple2)

# -------------------------------------------------------------

# to find index of an element in tuple :

# numbers = (53,64,24,785,534,85,43,85,345)

# x = numbers.index(534)
# print(x)

# -------------------------------------------------------------

# to count number of times an element occurs in tuple : 

x = (1,5,3,7,3,6,8,2,5,6,3,4,4,3,1)

print(x.count(3))