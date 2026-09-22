student = {
    "name": "Abeer",
    "age": 19,
    "city": "Karachi",
    "course": "BSSE"
}
student.update({"age" : 20})
student.update({"semester" : 3})
student.pop("city")

print(student.keys())

for key,value in student.items():
    print(key , ":" , value)