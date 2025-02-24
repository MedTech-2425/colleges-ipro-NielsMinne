#Vanaf nu beginnen we elke oefening op te lossen met functions (definitions) voor herbruikbaarheid van de code

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)  # BMI-formule
    return round(bmi, 2)  # Ronden op 2 decimalen

# Vraag de gebruiker om gewicht en lengte
weight = float(input("Voer uw gewicht in (kg): "))
height = float(input("Voer uw lengte in (m): "))

# Bereken de BMI en print het resultaat
bmi = calculate_bmi(weight, height) #gebruik van onze function die we hebben gemaakt
print(f"Uw BMI is: {bmi}")