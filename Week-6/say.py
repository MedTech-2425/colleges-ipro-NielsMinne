# name = input("Wat is je naam? ")

#1
# file = open("namen.txt", "a")
# file.write(name)
# file.close()

#2
# with open("namen.txt", "a") as file:
#     file.write(f"{name}\n")

#3 Lezen van een bestand
# with open("namen.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("Hallo," , line.rstrip())

#4
# with open("namen.txt", "r") as file:
#     for line in file:
#         print("Hallo," , line.rstrip())

#5
names = []

with open("namen.txt") as file:
    for line in file:
        names.append(line)

for name in sorted(names):
    print("Hello,", name.rstrip())



