def add_name():
    name= input("Voer je naam in: ")
    
    with open("namen.txt", "a") as file:
        file.write(name+ "\n")
    print(f"{name} is toegevoegd.")

def show_names():
    try:
        with open("namen.txt", "r") as file:
            names= file.readlines()
        # Sorteer de namen alfabetisch
        names.sort()
        for name in names:
            print(name.strip())
    except FileNotFoundError:
        print("Geen namen gevonden.")

def main():
    while True:
        print("\nWat wil je doen?")
        print("1. Voeg een naam toe")
        print("2. Toon alle namen")
        print("3. Stop")
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