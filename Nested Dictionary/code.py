students = {
    1: {"name": "Ravi", "marks": 85},
    2: {"name": "Sita", "marks": 90}
}

for student in students.values():
    print("Name:", student["name"])
    print("Marks:", student["marks"])
