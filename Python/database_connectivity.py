import mysql.connector

mydb = mysql.connector.connect(host="localhost", user ="root")
# print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("create database python_project;")
mycursor.execute("use python_project;")
# mycursor.execute("""create table student_detail
# (roll_no int,
#   name varchar(50),
#  course varchar(60) );
# """)

# mycursor.execute("""insert into student_detail values
#                 (1,'harpreet','Python'),(2,'Harman','MySQL'),(3,'Minakshi','Java'); """)

mycursor.execute("select * from student_detail;")
data = mycursor.fetchall()
# print(data)
for i in data:
    x,y,z = i
    # print(i)
    print(f"Roll No. = {x} \t Name = {y} \t Course = {z}")

mydb.commit()
mycursor.close()