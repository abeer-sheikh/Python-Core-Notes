# ye simple for loop se list mein number add karwaney ka tareeka hai
numbers = []
# for i in range(1,6):
#     numbers.append(i)
# print(numbers)


numbers = [i for i in range(1,11)]
print(numbers)


numbers = [i * i for i in range(1, 11)]

print(numbers)


numbers = [i for i in range(1,20) if i%2!=0]
print("Odd numbers : " , numbers)


n = int(input("Enter n : "))

numbers = [i * i * i for i in range(1, n + 1) if i % 2 == 0]

print("Cube of even numbers : ", numbers)