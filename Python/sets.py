# SETS : 

# used to store multiple items in single variable
# sets are unordered and unindexed
# set's elements are unchangeable but you can add or remove elements
# set do not allow duplicacy
# set is created by using curly brackets {}
# set's elements can be of any data type 

# set1 = {1,2,3,4,4,4,4,4}
# print(set1)
# print(type(set1))
# print(len(set1))

# for set 1 and True are same element
# similarly 0 and False are also same element

# set1 = {True,0,1,5.62,3,"Hello"}
# print(set1)

# set2 = {True,0,1,5.62,3,"Hello",False}
# print(set2)

# -------------------------------------------------------------

# to add an element in set:

# set1 = {1,2,3,4,5,6}

# set1.add(100)
# print(set1)

# to add multiple elements : 

# set1 = {1,2,3,4,5}
# set2 = {6,7,8,9,0}

# set1.update(set2)
# print(set1)

# -------------------------------------------------------------

# to remove an element : 

set1 = {"apple","mango","banana","guava"}
# set1.remove("kiwi")
# print(set1)

# set1.discard("kiwi")
# print(set1)

# set1.clear()
# print(set1)

# del set1
# print(set1)

# ---------------------------------------------------------------

# list1 = [1,2,3,4,5,6,34]

# set1 = set(list1)
# print(set1)

# ---------------------------------------------------------------

# set operations : 

# UNION : 

# set1 = {1,2,3,4}
# set2 = {3,4,5,6}

# set3 = set1.union(set2)
# print(set3)

# set3 = set1 | set2
# print(set3)

# set1.update(set2)
# print(set1)

# INTERSECTION : 

# set1 = {1,2,3,4}
# set2 = {3,4,5,6}

# set3 = set1.intersection(set2)
# print(set3)

# set3 = set1 & set2
# print(set3)

# set1.intersection_update(set2)
# print(set1)

# DIFFERENCE : 

# set1 = {1,2,3,4}
# set2 = {3,4,5,6}

# set3 = set1.difference(set2)
# print(set3)

# set3 = set2.difference(set1)
# print(set3)

# set3 = set1 - set2
# print(set3)

# set1.difference_update(set2)
# print(set1)

# DISJOINT : 

# set1 = {1,2,3,4}
# set2 = {3,4,5,6}

# print(set1.isdisjoint(set2))

set1 = {1,2,3,4}
set2 = {5,6,7,8}

print(set1.isdisjoint(set2))