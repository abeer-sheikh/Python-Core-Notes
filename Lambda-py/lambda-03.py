student_marks = int(input("Enter student marks between : (1-100) : "))
marks_check = lambda m: "Pass" if(m>=50 and m<=100) else ("Fail") if (m<50 and m>=0) else ("Invalid Marks")

print(marks_check(student_marks))