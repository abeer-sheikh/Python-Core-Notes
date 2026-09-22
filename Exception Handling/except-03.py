try:
    student = input("Enter student name : ")
    marks_1 = int(input("Enter marks 1 : "))
    marks_2 = int(input("Enter marks 2 : "))
    marks_3 = int(input("Enter marks 3 : "))
    total = marks_1+marks_2+marks_3
    avg = total/3
except ValueError:
    print("please enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Total :", total)
    print("Average :", avg)
    print("Result calculated successfully")           
finally:
    print("Program ended")

