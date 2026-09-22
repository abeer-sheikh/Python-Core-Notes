def largest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
result = largest(5,7,8)

print("Largest : " , result)