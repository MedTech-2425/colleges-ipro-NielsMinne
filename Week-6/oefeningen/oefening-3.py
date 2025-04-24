import csv

def add_hospital():
    name = input("Enter the hospital's name: ")
    location = input("Enter the hospital's location: ")
    capacity = input("Enter the hospital's capacity: ")

    with open("hospitals.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, location, capacity])
    print(f"Hospital {name} added.")

def show_hospitals():
    try:
        with open("hospitals.csv", "r") as file:
            reader = csv.reader(file)
            hospitals = list(reader)
        
        # Sort hospitals by name
        hospitals.sort(key=lambda x: x[0])
        
        for hospital in hospitals:
            print(f"Name: {hospital[0]}, Location: {hospital[1]}, Capacity: {hospital[2]}")
    except FileNotFoundError:
        print("No hospitals found.")

def update_hospital_data():
    name = input("Enter the name of the hospital you want to update: ")
    
    try:
        with open("hospitals.csv", "r") as file:
            reader = csv.reader(file)
            hospitals = list(reader)
        
        for hospital in hospitals:
            if hospital[0] == name:
                print(f"Hospital {name} found.")
                choice = input("What would you like to update? (location/capacity): ").lower()
                
                if choice == "location":
                    new_location = input("Enter the new location: ")
                    hospital[1] = new_location
                elif choice == "capacity":
                    new_capacity = input("Enter the new capacity: ")
                    hospital[2] = new_capacity
                else:
                    print("Invalid choice.")
                    return
                
                # Write the updated list back to the file
                with open("hospitals.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(hospitals)
                print(f"Data for {name} has been updated.")
                return
        print(f"Hospital {name} not found.")
    except FileNotFoundError:
        print("No hospitals found.")

def remove_hospital():
    name = input("Enter the name of the hospital you want to remove: ")
    
    try:
        with open("hospitals.csv", "r") as file:
            reader = csv.reader(file)
            hospitals = list(reader)
        
        # Filter the list to remove the hospital
        hospitals = [hospital for hospital in hospitals if hospital[0] != name]
        
        # Write the updated list back to the file
        with open("hospitals.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(hospitals)
        
        print(f"Hospital {name} has been removed.")
    except FileNotFoundError:
        print("No hospitals found.")

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a hospital")
        print("2. Show all hospitals")
        print("3. Update hospital data")
        print("4. Remove a hospital")
        print("5. Exit")
        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            add_hospital()
        elif choice == "2":
            show_hospitals()
        elif choice == "3":
            update_hospital_data()
        elif choice == "4":
            remove_hospital()
        elif choice == "5":
            print("Program exited.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()