#1
# with open("students.csv") as file:
#     for line in file:
#         name, location = line.rstrip().split(",")
#         print(f"{name} woont in {location}") 

#2 sorteren van data
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, location = line.rstrip().split(",")
#         students.append(f"{name} woont in {location}")

# for student in sorted(students):
#     print(student)

#3
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, location = line.rstrip().split(",")
#         student = {"name": name, "location": location}
#         students.append(student)

# for student in students:
#     print(f"{student["name"]} woont in {student['location']}")

#4
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, location = line.rstrip().split(",")
#         student = {"name": name, "location": location}
#         students.append(student)

# # def get_name(student):
# #     return student["name"]

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student["name"]} woont in {student['location']}")

#5 Writing csv writer
import csv

name = input("Wat is jou naam? ")
location = input("Waar woon je? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "location"])
    writer.writerow({"name": name, "location": location})

#6
# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "location": row["location"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student["name"]} woont in {student["location"]}")