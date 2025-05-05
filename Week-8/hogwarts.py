
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name" : name,"house": house}

# def main():
#     student = get_student()
#     if student["name"] == "Niels":
#         student["house"] == "Hufflepuff"
#     print(f"{student["name"]} from {student["house"]}")


# if __name__ == "__main__": 
#     main()

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Ravenclaw","Hufflepuff", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case _:
                return "✨"


def main():
    student = get_student()
    student._house = "Random"
    print(student)
    
    # print("Expecto Patronum!")
    # print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    try:
        return Student(name,house, patronus)
    except ValueError:
        print("Probeer opnieuw, niet geldig")

main()