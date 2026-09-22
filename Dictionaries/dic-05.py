student = {
    "name": "Abeer",
    "age": 19,
    "city": "Karachi",
    "course": "BSSE"
}

print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
    print(key , ":" , value)