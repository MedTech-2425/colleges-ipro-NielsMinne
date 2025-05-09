
# Laat de gebruiker een cijfer invoeren (0–10). Geef daarna een beoordeling:

# - 0–5.4: “Onvoldoende”
# - 5.5–6.4: “Voldoende”
# - 6.5–7.9: “Goed”
# - 8–10: “Uitstekend”

# 👉 **Extra uitdaging:** Controleer of het ingevoerde cijfer binnen 0–10 valt, anders geef een foutmelding.


try:
    number = float(input("Voer een cijfer in: "))
    if 0 <= number <= 10:
        if number <= 5.4:
            print("onvoldoende")
        elif number <= 6.4:
            print("Voldoende")
        elif number <= 7.9:
            print("Goed")
        elif number <= 10:
            print("Uitstekend")
    else:
        print("Jou cijfer valt niet tussen de range")

except ValueError:
    print("Fout: Voer een geldig getal")
