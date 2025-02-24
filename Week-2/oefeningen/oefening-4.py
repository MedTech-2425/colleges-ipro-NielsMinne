def calculate_dosage(weight):
    dosage = weight * 2  # 2 mg per kg lichaamsgewicht
    return round(dosage, 1)  # Ronden op 1 decimaal

# Vraag de gebruiker om het gewicht van de patiënt
weight = float(input("Voer het gewicht van de patiënt in (kg): "))

# Bereken de dosering en print het resultaat
dosage = calculate_dosage(weight)
print(f"De patiënt moet {dosage} mg van het medicijn krijgen.")