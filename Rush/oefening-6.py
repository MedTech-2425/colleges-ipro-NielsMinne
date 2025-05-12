# Speler gooit een dobbelsteen (1–6) totdat hij exact 20 bereikt. Bij een totaal boven 20 is hij “af”.

# Gebruik `random.randint(1, 6)` en toon alle worpen.

# 👉 **Extra:** Laat twee spelers tegen elkaar spelen om de beurt.

import random

def player_turn(name):
    total = 0
    rolls = []
    
    while True:
        print(f"\n{name}'s turn → Total: {total}")
        choice = input("Roll or stop? (r/s): ").strip().lower()
        if choice == 'r':
            roll = random.randint(1, 6)
            rolls.append(roll)
            total += roll
            print(f"{name} rolled a {roll} → New total: {total}")
            if total > 20:
                print(f"{name} is BUSTED!")
                return 0
        elif choice == 's':
            print(f"{name} stops at {total}")
            return total
        else:
            print("Please type 'r' to roll or 's' to stop.")

# Game start
print("🎲 Game to reach exactly 20! Closest without going over wins.")

score1 = player_turn("Player 1")
score2 = player_turn("Player 2")

print("\n🏆 Result:")
if score1 > score2:
    print("Player 1 wins!")
elif score2 > score1:
    print("Player 2 wins!")
else:
    print("It's a tie!")
