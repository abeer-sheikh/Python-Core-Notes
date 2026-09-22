n = int(input("Enter n : "))
count = 0
# while loop
while(n>0):
    n = n//10
    count+=1
print("Count : " , count)