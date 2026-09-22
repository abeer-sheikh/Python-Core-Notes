a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))


largest = lambda x,y,z: (x) if (x>y and x>z) else (y) if (y>x and y>z) else (z)

print(largest(a,b,c))