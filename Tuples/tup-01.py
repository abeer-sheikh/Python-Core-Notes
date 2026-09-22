l = (10, 5, 20, 15, 10, 30)
total = 0
for numbers in l:
    total+=numbers
print("Tuples Sum : " , total)
print("Largest : " , max(l))
print("Smallest : " , min(l))
print("10 Count : " , l.count(10))
print("Last Element : " , l[-1])     