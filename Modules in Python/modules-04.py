import datetime
import random

now = datetime.datetime.now()

name = input("Enter your name : ")

maths_marks = int(input("Enter maths marks : "))
physics_marks = int(input("Enter physics marks : "))
computer_marks = int(input("Enter computer marks : "))

total = maths_marks+physics_marks+computer_marks
avg = total/3

result_id = random.randint(1,100)

print("\n---- Student Result ----")
print("Name : " , name)
print("Result ID : " , result_id)
print("Total marks : " , total)
print("Avergae marks : " , avg)
print("Date : ", now.strftime("%d-%m-%Y"))