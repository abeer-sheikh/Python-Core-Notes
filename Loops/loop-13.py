# reverse number

n = int(input("Enter n : "))
reverse = 0
# while loop
while(n>0):
    digit = n % 10
    n = n // 10
    reverse = reverse * 10 + digit
print("Reverse : " ,reverse)    