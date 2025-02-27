try: 
    a = int(input("Geef het eerste getal: "))
    b = int(input("Geef het tweede getal: "))
    result = a / b;
    if a > 5:
        raise ValueError("het getal mag niet groter zijn dan 5")
    print("Het resultaat is:", result)
except Exception as e:
    print(f"Er is een fout opgetreden:{e}")
else:
    print("else blok uitgevoerd")
finally:
    print("finally blok")

