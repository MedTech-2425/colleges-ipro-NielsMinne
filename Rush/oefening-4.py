
# Laat de gebruiker een profiel aanmaken met naam, leeftijd, land, favoriete programmeertaal. Sla dit op in een dictionary.

# Maak een functie `show_profile(profile_dict)` die de data netjes print.

# 👉 **Extra:** Voeg een controle toe: als leeftijd < 13, print dan een waarschuwing: *"Deze app is bedoeld voor 13+."*

def main():
    name = input("Wat is uw naam? ")
    age = input("Wat is je leeftijd? ")
    country = input("Waar ben je geboren? ")
    language = input("Wat is je favoriete taal? ")

    profile = {
        "name" : name, 
         "age" : age, 
        "country" : country, 
         "language" : language, 
    }

    show_profile(profile)



def show_profile(profile):
    print("GebruikersProfiel:")
    print(f"Naam: {profile["name"]}")
    print(f"Age: {profile["age"]}")
    print(f"Country: {profile["country"]}")
    print(f"Language: {profile["language"]}")

    if int(profile["age"]) < 13:
        print("Deze app is bedoeld voor 13+.")



if __name__ == "__main__":
    main()