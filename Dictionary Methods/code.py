student = {"name": "Ravi", "age": 18, "marks": 90}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

student.update({"age": 19})
print(student)

student.pop("marks")
print(student)
