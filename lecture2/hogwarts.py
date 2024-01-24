#a list of dictonarys
students = [
    {"name": "Hermione", "house": "Gryffindor", "patrounus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patrounus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patrounus": "Jack Rustell terrier"},
    {"name": "Draco", "house": "Slytherin", "patrounus": None}
]

for student in students:
    print(student["name"], student["house"], student["patrounus"], sep=", ")

'''
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep = ", ")

    
#uses student's name acts as the indicator of location 
print(students["Hermione"])

#creates the var "students" and makes is a list 
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# len means length, uses var "students" to tell how long a list is 
for i in range(len(students)):
    print(i + 1, students[i])
    '''