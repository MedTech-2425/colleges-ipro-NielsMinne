# Laat de gebruiker een woord raden, letter voor letter (gebruik underscores: `h_ l _`).

# Beperk het aantal pogingen tot 6. Houd de juiste en foute letters bij.

# Laat het spel eindigen bij winst of verlies.

# 👉 **Extra:** Voeg een woordlijst toe en kies een willekeurig woord (import `random`).

import random

# Woordlijst
words = ["python", "computer", "spelletje", "programmeren", "galgje", "taart"]

# Kies een willekeurig woord
word = random.choice(words)
guessed_letters = []
wrong_letters = []
max_wrong = 6

print("🎯 Raad het woord! Je mag maximaal 6 fouten maken.")

while True:
    # Toon woord met underscores
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print("\nWoord:", " ".join(display))
    print("Foute letters:", " ".join(wrong_letters))
    print(f"Fouten: {len(wrong_letters)} / {max_wrong}")

    # Check einde
    if len(wrong_letters) >= max_wrong:
        print("\n💥 Verloren! Het woord was:", word)
        break
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Gewonnen! Het woord was:", word)
        break

    # Vraag gebruiker om letter
    guess = input("Raad een letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Geef één letter.")
        continue

    if guess in guessed_letters or guess in wrong_letters:
        print("⚠️ Die letter had je al geprobeerd.")
        continue

    # Verwerk gok
    if guess in word:
        guessed_letters.append(guess)
        print("✅ Goed!")
    else:
        wrong_letters.append(guess)
        print("❌ Fout!")