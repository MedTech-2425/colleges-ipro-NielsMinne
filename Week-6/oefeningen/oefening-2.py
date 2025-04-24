import csv

def add_student():
    name = input("Enter the student's name: ")
    location = input("Enter the student's location: ")
    
    # Add student to the CSV file
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, location])
    print(f"Student {name} added.")

def show_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            students = list(reader)
        
        # Sort students by name
        students.sort(key=lambda x: x[0])
        
        for student in students:
            print(f"Name: {student[0]}, Location: {student[1]}")
    except FileNotFoundError:
        print("No students found.")

def remove_student():
    name = input("Enter the name of the student you want to remove: ")
    
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            students = list(reader)
        
        # Filter the list to remove the student
        students = [student for student in students if student[0] != name]
        
        # Write the updated list back to the file
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)
        
        print(f"Student {name} has been removed.")
    except FileNotFoundError:
        print("No students found.")

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a student")
        print("2. Show all students")
        print("3. Remove a student")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            print("Program exited.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()