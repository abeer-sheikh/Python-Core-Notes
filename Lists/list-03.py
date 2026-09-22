l = [12, 5, 8, 20, 3, 15]
total = 0

#for loop
for numbers in l:
    total+=numbers
print("Sum : " , total)

#largest number:
print("Largest : " , max(l))
print("Smallest : " , min(l))

#append:
l.append(30)
#remove:
l.remove(5)
#ascending order mein banadiya
l.sort()

print(l)
