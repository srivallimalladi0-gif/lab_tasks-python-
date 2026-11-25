students = [
    {"name": "Ravi", "marks": 85},
    {"name": "Sita", "marks": 95},
    {"name": "Ram", "marks": 70},
    {"name": "Priya", "marks": 80}
]

# Ascending order
ascending = sorted(students, key=lambda x: x["marks"])

print("Ascending Order:")
for student in ascending:
    print(student)

# Descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("\nDescending Order:")
for student in descending:
    print(student)
