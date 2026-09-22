try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print(num1/num2)
except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Program Successfully completed")
finally:
    print("Program ended")

# agar error na aye to try chalta hai agar error aye to except chalta hai or ye hum isi liye use kartey hein ke program crash na ho or ZeroDivisionError hum isi liye use kartey hein ke agar koi value python mein divide na hosakey to jo iskey andar statement hai to wo print hojaye or error na aye jesey ke 0 se divide nahi hosakta to error ke bajaye iskey andar ki statement print hojayegi or ValueError isi liye use kartey hein for suppose hum int ka input le rahey hein lekin user string input mein dedey to error nahi aayega balkey andar ke print statement print hojayegi that's it. or else wab chalta hai jab try block chaley or error na aye. or finally har haal mein chalega bhaley error aye yan na aye.