# Vraag de gebruiker om een getal (bijv. 4). Print daarna de tafel van dat getal van 1 t/m 10:

# 4 x 1 = 4
# 4 x 2 = 8
# ...

# 👉 **Extra uitdaging:** Vraag ook tot welk getal de tafel moet gaan (bijv. 20), en gebruik dit als eindwaarde in de loop.


number = int(input("Geef een getal: "))

end = int(input("Tot welke tafel wil je gaan:"))

for i in range(end):
    print(f"{number} x {i + 1} = {(i +1) * number}")