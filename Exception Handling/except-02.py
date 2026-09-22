try:
    num1 = int(input("Enter first number : "))
    op = (input("Enter an operator : ('+' , '-'  '*' , '/') : "))
    num2 = int(input("Enter second number : "))
    if(op=='+'):
        print("Result : " , num1+num2)
    elif(op=='-'):
        print("Result : " , num1-num2)
    elif(op=='*'):
        print("Result : " , num1*num2)
    elif(op=='/'):
        print("Result : " , num1/num2)    
    else:
        print("Invalid Operator")
except ValueError:
    print("please enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Calculation Done")
finally:
    print("Program ended")                                
