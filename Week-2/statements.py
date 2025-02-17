# number = int(input("Geef een getal in: "))

# if number >= 0:
#     print("Het getal is positief.")
# else:
#     print("Het getal is negatief")

# if number > 0:
#     print("Het getal is positief.")
# if number > 5: 
#     print("Het getal is negatief")
# if number == 0:
#     print("Het getal is nul")

#elif
# if number > 0:
#     print("Het getal is positief")
# elif number < 0:
#     print("Het getal is Negatief")
# else:
#     print("Het getal is nul")

#grades

# grade = int(input("Geef je cijfer in: "))


# if grade >= 60:
#     print("Je hebt een D")
# elif grade >= 70:
#     print("Je hebt een C")
# elif grade >= 80:
#     print("Je hebt een B")
# elif grade >= 90:
#     print("Je hebt een A")
# else:
#     print("Je bent gebuisd, foei!")


#match case
day = input("Welke dag is het vandaag? ").strip().lower()

match day:
    case "maandag":
        print("Het is maandag, begin van de week!")
    case "vrijdag":
        print("Het is vrijdag, bijna weekend!")
    case "zondag":
        print("Het is zondag, tijd om te ontspannen")
    case _:
        print("Dit is een andere dag van de week ")