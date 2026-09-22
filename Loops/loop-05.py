# factorial question:

n = int(input("Enter a number : "))
fact = 1
# for loop
for i in range(1,n+1):
    fact*=i
print(f"Factorial of {n} is : {fact}")
