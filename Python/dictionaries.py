# DICTIONARY IN PYTHON : 

# dictinary is used to store elements in key-value pair
# is ordered, changeable and do not allow duplicacy(for keys)
# dictionary is created by using {}
# Syntax : 

# dict_name = {
# key1 : val1,
# key2 : val2,
# key3 : val3,
# ...........
# }

# student_detail = {
#     "name" : "Harpreet Kaur",
#     "Course" : "B.tech",
#     "Age" : 22,
#     "email" : "harpreet@gmail.com",
#     "email1" : "harpreet@gmail.com"
# }

# print(student_detail)
# print(type(student_detail))
# print(len(student_detail)) 

# ------------------------------------------------------------------
# dict() constructor : 

# my_dict = dict(name = "Harpreet", course = "BCA",age = 78)
# print(my_dict)

# ------------------------------------------------------------------

# ACCESSING DICT ITEMS : 

# student_detail = {
#     "name" : "Harpreet Kaur",
#     "Course" : "B.tech",
#     "Age" : 22,
#     "email" : "harpreet@gmail.com" }

# print(student_detail["email"])

# x = student_detail.get("Course")
# print(x)

# x = student_detail.keys()
# print(x)

# x =student_detail.values()
# print(x)

# x =student_detail.items()
# print(x)

# ------------------------------------------------------------------
# CHANGE DICTIONARY VALUES : 

# student_detail = {
#     "name" : "Harpreet Kaur",
#     "Course" : "B.tech",
#     "Age" : 22,
#     "email" : "harpreet@gmail.com" }

# student_detail["Age"] = 33

# print(student_detail)

# changes = {
#     "Age" : 33,
#     "email" : "harpreetkaur@gmail.com"
# }

# student_detail.update(changes)
# print(student_detail)

# ------------------------------------------------------------------
# ADD DICTIONARY Item : 

# student_detail = {
#     "name" : "Harpreet Kaur",
#     "Course" : "B.tech" }

# student_detail["Age"] = 33
# print(student_detail)

# changes = {
#     "Age" : 33,
#     "email" : "harpreetkaur@gmail.com"
# }

# student_detail.update(changes)
# print(student_detail)

# ------------------------------------------------------------------
 
# Delete dictionary items: 

# student_detail = {
#     "name" : "Harpreet Kaur",
#     "Course" : "B.tech",
#     "Age" : 22,
#     "email" : "harpreet@gmail.com" }

# student_detail.pop("email")
# print(student_detail)

# student_detail.popitem()
# print(student_detail)

# student_detail.clear()
# print(student_detail)

# del student_detail["Age"]
# print(student_detail)

# del student_detail
# print(student_detail)

# ------------------------------------------------------------------

# TO COPY A DICTIONARY : 

# student_detail = {
#     "name" : "Harpreet Kaur",
#     "Course" : "B.tech",
#     "Age" : 22,
#     "email" : "harpreet@gmail.com" }

# student_detail_copy = student_detail.copy()
# print(student_detail_copy)

# ------------------------------------------------------------------

# NESTED DICTIONARY : 

# student_dtails= {
#     'student1' : {
#         "name" : "Harpreet",
#         "course" : "BCA"},
#     "student2" : {
#         "name" : "Aman",
#         "course": "MCA"
#     },
#     "student3" : {
#         "name" : "Priya",
#         "course": "B.tech."
#     }
# }

# print(student_dtails["student2"]["name"])

