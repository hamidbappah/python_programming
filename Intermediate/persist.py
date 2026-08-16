import json

students = [
    {"name": "Adaeze", "gpa": 4.5},
    {"name": "Bello",  "gpa": 3.8},
]

# write once, read anywhere
with open("students.json", "w") as f:
    json.dump(students, f, indent=2)

with open("students.json") as f:
    data = json.load(f)
