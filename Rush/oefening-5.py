# Maak een rekenmachine die herhaaldelijk input vraagt tot de gebruiker “stop” typt. Ondersteun +, -, *, /, en vermenigvuldiging met macht (**).

# Bij verkeerde input (zoals “5 ++ 2”) moet een foutmelding komen.

# 👉 **Extra:** Voeg geschiedenis toe: print alle berekeningen als de gebruiker “geschiedenis” typt.

history = []

print("Welcome to the calculator. Type 'stop' to quit or 'history' to view past calculations.")

while True:
    expr = input("Enter a calculation: ").strip().lower()
    
    if expr == "stop":
        print("Program stopped.")
        break
    elif expr == "history":
        if history:
            print("\n--- History ---")
            print("\n".join(history))
            print("---------------\n")
        else:
            print("No history yet.")
        continue

    try:
        result = eval(expr) #Eval is een functie die text input omzet naar berekeningen
        entry = f"{expr} = {result}"
        history.append(entry)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)