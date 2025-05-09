
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

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

class Student(Wizard):
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        # if house not in ["Gryffindor", "Ravenclaw","Hufflepuff", "Slytherin"]:
        #     raise ValueError("Invalid House")
        super().__init__(name)
        # self.house = house
        # self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
        
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name,house, patronus)

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
            
    def speak(self):
        return "Ik ben een student van Hogwarts"
    
class Gryffindor(Student):
    def speak(self):
        return "Moed en lef! Ik ben een Gryffindor!"

class Slytherin(Student):
    def speak(self):
        return "Ambitie en sluwheid. Ik ben een Slytherin."

class Ravenclaw(Student):
    def speak(self):
        return "Wijsheid eerst! Ravenclaw, natuurlijk."

class Hufflepuff(Student):
    def speak(self):
        return "Loyaliteit en hard werk, dat is Hufflepuff!"


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


def main():
    # wizard = Wizard("Albus")
    # student = Student("Harry", "Ravenclaw", "Stag")
    # professor = Professor("Severus", "Defense against the Dark Arts")

    # print(wizard.name)
    # print(student.name)
    # print(professor.name)

    
    # print("Expecto Patronum!")
    # print(student.charm())

    students = [
        Student("Niels"),
        Gryffindor("Harry"),
        Slytherin("Draco"),
        Ravenclaw("Luna"),
        Hufflepuff("Cedric")
    ]

    for student in students:
        print(f"{student.name} zegt {student.speak()}")




main()