# Vraag de gebruiker een wachtwoord te kiezen.

# Voer checks uit:

# - Minimaal 8 tekens
# - Bevat hoofdletter, kleine letter, cijfer en speciaal teken

# Print wat er mist als het niet voldoet.

# 👉 **Extra:** Laat de gebruiker opnieuw proberen tot het wachtwoord goed is.

import string

while True:
    password = input("Kies een wachtwoord: ")

    errors = []

    if len(password) < 8:
        errors.append("minimaal 8 tekens")
    if not any(c.islower() for c in password):
        errors.append("kleine letter")
    if not any(c.isupper() for c in password):
        errors.append("hoofdletter")
    if not any(c.isdigit() for c in password):
        errors.append("cijfer")
    if not any(c in string.punctuation for c in password):
        errors.append("speciaal teken")

    if not errors:
        print("Wachtwoord is sterk!")
        break
    else:
        print("Ongeldig wachtwoord, je mist:", ", ".join(errors))