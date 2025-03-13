# n = int(input("Geef me een nummer boven 5? "))

# if n < 5:
#     n = int(input("Geef me een nummer boven 5? "))
#     if n < 5:
#         n = int(input("Geef me een nummer boven 5? "))
#         if n < 5:
#             n = int(input("Geef me een nummer boven 5? "))

# while True:
#     n = int(input("Geef me een positief nummer? "))
#     if n < 0:
#         continue
#     else:
#         break

# while True:
#     n = int(input("Hoeveel keer moet ik Milan printen? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Milan")

# ---------------------------

# def main():
#     number = get_number()
#     blub(number)

# def get_number():
#     while True:
#         n = int(input("Hoeveel keer moet ik blub printen? "))
#         if n > 0:
#             return n

# def blub(n):
#     for _ in range(n):
#         print("Blub")

# main()

# ----------------------------------

# students = ["Jorit", "Andreas", "Aaron", "Igor"]


# # for student in students:
# #     print(student)

# for i in range(len(students)):
#     print(i + 1, ":", students[i])


#None

# def check_numbers(n):
#     if n < 0:
#         return None
#     return n

# print(check_numbers(3))
# print(check_numbers(-1))

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            # print("Je getal is geen nummer")
            pass
        else:
            break
    
    return x 

main()

    