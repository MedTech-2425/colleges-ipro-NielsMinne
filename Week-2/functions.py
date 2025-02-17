
def greet(name="Guest"):
    print("Hallo,", name)

name = input("What is your name? ")

greet()
greet(name)

# def introduce(name, age):
#     print("Hello, my name is " + name + " and I am " + str(age) + " years old.")


# name = input("What is your name? ")
# age = int(input("What is your age? "))

# introduce(name, age)


# def add(a,b):
#     return a + b

# result = add(5,3)
# print(add(5,8))

def print_names(*names):
    for name in names:
        print(name)


