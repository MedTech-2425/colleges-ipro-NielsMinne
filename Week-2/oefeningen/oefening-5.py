def diagnose(test_score):
    if test_score >= 80:
        return "Goede gezondheid"
    elif 50 <= test_score < 80:
        return "Er is enige bezorgdheid"
    else:
        return "Zorgwekkend, dringende medische aandacht vereist"

# Voorbeeld:
result = diagnose(72)
print(result )  # Output: Er is enige bezorgdheid