#if statement

number = int(input("Geef een getal in: "))
if number > 10:
    print("Het getal is groter dan 10.")

#if - else statement

number = int(input("Geef een getal in: "))

if number > 0:
    print("Het getal is positief")
else:
    print("Het getal is negatief")
    


#waarom niet alleen ifs? 

number = int(input("Geef een getal in: "))

if number > 0:
    print("Het getal is positief.")
if number > 0:
    print("Het getal is negatief.")
if number == 0:
    print("Het getal is nul.")
    
#deze code zal altijd alle statements checken voor ook al is het eerste statement al true

# elif statement

number = int(input("Geef een getal in: "))

if number > 0:
    print("Het getal is positief.")
elif number < 0:
    print("Het getal is negatief.")
else:
    print("Het getal is nul.")
    
    
#volgorde van if else doet er toe ( hoogste waarde eerst)
#voorbeeld met grades

grade = int(input("Geef je cijfer in: "))

if grade >= 90:
    print("Je hebt een A.")
if grade >= 80:
    print("Je hebt een B.")
if grade >= 70:
    print("Je hebt een C.")
if grade >= 60:
    print("Je hebt een D.")

#eerst foutief

grade = int(input("Geef je cijfer in: "))

if grade >= 60:
    print("Je hebt een D.")
elif grade >= 70:
    print("Je hebt een C.")
elif grade >= 80:
    print("Je hebt een B.")
elif grade >= 90:
    print("Je hebt een A.")
else:
    print("Je hebt een F.")
    

#juist volgorde

grade = int(input("Geef je cijfer in: "))

if grade >= 90:
    print("Je hebt een A.")
elif grade >= 80:
    print("Je hebt een B.")
elif grade >= 70:
    print("Je hebt een C.")
elif grade >= 60:
    print("Je hebt een D.")
else:
    print("Je hebt een F.")
    
#match case statement
day = input("Enter the day of the week: ")
day = day.strip().lower()

match day:
    case "maandag":
        print("Het is maandag, begin van de week!")
    case "vrijdag":
        print("Het is vrijdag, bijna weekend!")
    case "zondag":
        print("Het is zondag, tijd om te ontspannen.")
    case _:
        print("Dit is een andere dag van de week.")