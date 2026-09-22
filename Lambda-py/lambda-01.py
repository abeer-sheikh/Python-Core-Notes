# lambda parameter: expression
square = lambda n:n * n
print(square(5))

addition = lambda a,b: a+b
print(addition(5,5))

# lambda n: value_if_true if condition else value_if_false

check = lambda n: "Even" if n%2==0 else "Odd"
print(check(8))

largest = lambda a,b: (a , "is largest") if a>b else (b , "is largest")

print(largest(5,10))