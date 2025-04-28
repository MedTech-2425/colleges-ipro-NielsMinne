# Global Variables

# def main():
#     balance = 0
#     print("Balance", balance)
#     deposit(350, balance)
#     withdraw(20, balance)
#     print("Balance:", balance)

# def deposit(n, balance):
#     balance += n

# def withdraw(n, balance):
#     balance -= n


# if __name__ == "__main__":
#     main()

#----------

#Constante

# WOOFS = 5

# for _ in range(WOOFS):
#     print("Woof")

#---------

# name = "Hermione"  #String
# age = 17        # Int
# height = 1.63   # Float


# def meow(n: int) -> None:
#     for _ in range(n):
#         print("Meow")

# number: int = int(input("Number: "))
# meow(number)

#---------------
#Docstring

# def meow(n: int) -> str:
#     """
#     Meow n times.

#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: if n is not an int
#     :return: A string of meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n



#----------------------------

# Map - Filter

# def main():
#     yell("This", "is", "Ipro", "test")

# def yell(*words):
#     uppercased = map(str.upper, words)
#     print(*uppercased)

# if __name__ == "__main__":
#     main()


students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Hermione", "house": "Gryffindor"},
]

def is_gryffindor(student):
    return student['house'] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)