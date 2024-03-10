data = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in data:
    print(student["name"], student["house"], student["patronus"], sep=": ")
"""
data = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in data:
    print(student, data[student], sep=" - ")
"""
