n = int(input("Enter n : "))

original = n
reverse = 0
count = 0

while(n>0):
    n = n//10
    count+=1
print("Count : " , count)

n = original
while(n>0):
    digit = n%10
    n = n//10
    reverse = reverse*10+digit
print("Reverse : " , reverse)    
