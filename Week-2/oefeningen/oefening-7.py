def check_dose(dose):
    try:
        dose= float(dose)  # probeer om de dosering om te zetten naar een float
        if dose<= 0:
            raise ValueError("De dosering moet een positief getal zijn.")
        return f"De dosering is {dose} mg."
    except ValueError as e:
        return f"Fout: {e}"

# Voorbeeld:
result = check_dose("50")
print(result )  # Output: De dosering is 50.0 mg.

result = check_dose("-5")
print(result )  # Output: Fout: De dosering moet een positief getal zijn.

result = check_dose("onbekend")
print(result )  # Output: Fout: kon geen conversie naar float maken: 'onbekend'