#loops -> Herhalingsstructuren

# for - loop
# Voorbeeld van een for-loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#range (eenvoudige reeks getallen genereren -> handig bij for loops)
# Voorbeeld met range()
for i in range(5):  # Dit genereert de getallen 0 tot 4
    print(i)

#range kan in stapgrootte
# Voorbeeld met een stapgrootte
for i in range(0, 10, 2):  # Stapgrootte van 2
    print(i)

# #while loop 
# i = 0

# # while i <= 5:
# #     print(i)
# #     i += 1

# #break en continue

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

#nested loops
matrix = [[1,2,3], [4,5,6], [7,8,9]]

for row in matrix:
    print(row)
    for num in row:
        print(num)

