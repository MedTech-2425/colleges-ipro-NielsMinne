<<<<<<< HEAD
# printen van een string
print("Hello, MedTech!")

# Wat bij een fout?
print("Hello, MedTech!"
# SyntaxError: '(' was never closed

#input laat je iets invoeren in de terminal 
print("Wat is je naam?")
input()

#input kan ook een string bevatten
input("Wat is je naam? ")

=======

# PRINT
# print()-functie van python
print("Hallo, Medtech!")

# ------------------------------------------- #

# Errors in code
# print("Hallo, Medtech!"

# ------------------------------------------- #
      
# INPUT
#input()-functie van python (2 lijnen of 1 lijn)

#2 lijnen
print("Wat is je naam? ")
input()

#1 lijn
input("Wat is je naam? ")

# ------------------------------------------- #

# VARIABLES
#(Opslaan van een waarde in een 'container')
name = "Niels"
print(name)

#input functie retourneert altijd de waarde die je intypt, en deze slaan we op in de variabele 'name'
name = input("Wat is je naam? ")
print("Hallo, " + name)

# ------------------------------------------- #

#STRINGS

#Onder elkaar
print("Hallo, ")
print(name)

# Aan elkaar (String concatenation)
print("Hallo, " + name)

#meerdere argumenten (Sep is de seperator (default is deze met een spatie, indien je dit wil overschrijven -> ))
print("Hello, ",name, sep="")

# String met quotes binnenin (2 manieren)
print('Hello, "Friend"')
print("Hello, \"Friend\"")

# f-strings 
# (deze gaan vooraf met een f en variabelen plaats je tussen { } -> curly brackets)
# Indien je een nieuwe lijn wil kan je dit doen met \n
print(f"Hello, {name} \nDit is een nieuwe lijn")

# ------------------------------------------- #

# STRING METHODS

# Om de output aan te passen van de variabele, LET OP: Deze methoden werken enkel op strings -> tekst

#strip() (spaties weg te halen -> Links en rechts van de output (niet tussenin!))
name = name.strip()

# #capitalize() (eerste woord met een hoofdletter)
name = name.capitalize()

# #title() (elk woord hoofdletter)
name = name.title()

#Het is ook mogelijk om methoden te 'chainen' -> na elkaar aanroepen van methodes
name = name.strip().title()

print(f"Hello, {name}")
>>>>>>> 92b09b95b4350dc1a5bcc122ff2e0e6391ccaa84

