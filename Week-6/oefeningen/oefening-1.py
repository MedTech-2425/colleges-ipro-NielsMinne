def add_name():
<<<<<<< HEAD
    name = input("Voer je naam in: ")

    try:
        with open("namen.txt", "a") as file:
            file.write(name + "\n")
        print(f"{name} is toegevoegd.")
    
    except FileNotFoundError:
        print("Error")
=======
    name= input("Voer je naam in: ")
    
    with open("namen.txt", "a") as file:
        file.write(name+ "\n")
    print(f"{name} is toegevoegd.")
>>>>>>> d160e89d75e3bdf4a1d27551b9c7aacba36124a9

def show_names():
    try:
        with open("namen.txt", "r") as file:
<<<<<<< HEAD
            names = file.readlines()
        
=======
            names= file.readlines()
        # Sorteer de namen alfabetisch
>>>>>>> d160e89d75e3bdf4a1d27551b9c7aacba36124a9
        names.sort()
        for name in names:
            print(name.strip())
    except FileNotFoundError:
        print("Geen namen gevonden.")

<<<<<<< HEAD

=======
>>>>>>> d160e89d75e3bdf4a1d27551b9c7aacba36124a9
def main():
    while True:
        print("\nWat wil je doen?")
        print("1. Voeg een naam toe")
        print("2. Toon alle namen")
        print("3. Stop")
<<<<<<< HEAD
        choice = input("Kies een optie (1/2/3)")

        if choice == "1":
            #hier komt iets
            add_name()
        elif choice == "2":
            #hier komt functie 2
            show_names()
        elif choice == "3":
            print("Programma is gestopt")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw")



if __name__ == "__main__":
    main()
=======
        choice= input("Kies een optie (1/2/3): ")

        if choice== "1":
            add_name()
        elif choice== "2":
            show_names()
        elif choice== "3":
            print("Programma gestopt.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main()
>>>>>>> d160e89d75e3bdf4a1d27551b9c7aacba36124a9
