
#functie met standaardwaarde
def greet(name="Guest"):
    print("Hallo,", name)

name = input("What is your name? ")

greet()
greet(name)

#functie met meerdere parameters
def introduce(name, age):
    print("Hello, my name is " + name + " and I am " + str(age) + " years old.")


name = input("What is your name? ")
age = int(input("What is your age? "))

introduce(name, age)

#Functie die data returned
def add(a,b):
    return a + b

result = add(5,3)
print(result)
print(add(5,8))

#lijst printen van namen (*args) -> meerdere argumenten
def print_names(*names):
    for name in names:
        print(name)

print_names("Niels", "Miguel", "Andreas", "Tianny")


