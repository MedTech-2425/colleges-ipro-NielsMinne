# Maak een functie `calculate_bmi(weight, length)` die de BMI uitrekent (gewicht / lengte²). Laat de gebruiker beide invoeren en print het resultaat.

# 👉 **Extra uitdaging:** Print ook de beoordeling:

# - <18.5: Ondergewicht
# - 18.5–24.9: Gezond
# - 25–29.9: Overgewicht
# - ≥30: Obesitas


def main():
    weight = input("Hoeveel kg weeg je? ")
    length = input("Hoe groot ben je (m)? ")
    calculate_bmi(weight, length)



def calculate_bmi(weight, length):
    return weight / length * length

def print_bmi_result(bmi):
    if bmi < 18.5:
        print("Ondergewicht")
    elif 18.5 <= bmi <= 24.9:
        print("Gezond")
    elif 25 <= bmi <= 29.9:
        print("Overgewicht")
    else:
        print("Obesitas")

if __name__ == "__main__":
    main()