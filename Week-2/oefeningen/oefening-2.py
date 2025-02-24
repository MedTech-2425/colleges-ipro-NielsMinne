def check_heart_rate(heart_rate):
    if heart_rate < 60:
        return "Uw hartslag is te laag!"
    elif heart_rate > 100:
        return "Uw hartslag is te hoog!"
    else:
        return "Uw hartslag is normaal."

# Vraag de gebruiker om hun hartslag in rust
heart_rate = int(input("Voer uw hartslag in rust in: "))

# Controleer de hartslag en print het resultaat
message = check_heart_rate(heart_rate)
print(message)