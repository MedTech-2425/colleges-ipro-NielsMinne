#Set
#ongeordende verzameling van UNIEKE elementen

# Een set maken met accolades
new_set = {1, 2, 3, 4, 5}
print(new_set)  # Output: {1, 2, 3, 4, 5}

# Een set maken met de set() functie
new_set2 = set([1, 2, 3, 4, 5])
print(new_set2)  # Output: {1, 2, 3, 4, 5}


#LET OP - een lege set moet worden aangemaakt met set() niet met {}
empty_set = set()  # Correct
empty_dict = {}    # Dit maakt een lege dictionary

#elementen toevoegen of verwijderen 
#toevoegen
new_set = {1, 2, 3}
new_set.add(4)  # Eén element toevoegen
print(new_set)  # Output: {1, 2, 3, 4}

new_set.update([5, 6, 7])  # Meerdere elementen toevoegen (list meegeven)
print(new_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

#verwijderen
new_set.remove(3)  # Verwijdert 3
print(new_set)

new_set.discard(10)  # Probeert 10 te verwijderen, maar geeft GEEN fout als het ontbreekt

removed_element = new_set.pop()  # Verwijdert een willekeurig element
print("Verwijderd:", removed_element)



# Set Operations

#union (verenigen)
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2  # Met de `|` operator
print(union_set)  # Output: {1, 2, 3, 4, 5}

union_set = set1.union(set2)  # Met de `union()` methode
print(union_set)  # Output: {1, 2, 3, 4, 5}

#intersect -> alle gemeenschapelijke elementen
intersect_set = set1 & set2  # Met `&` operator
print(intersect_set)  # Output: {3}

intersect_set = set1.intersection(set2)  # Met `intersection()` methode
print(intersect_set)  # Output: {3}

#difference -> Geeft de elementen terug die alleen in de set zitten 
diff_set = set1 - set2  # Met `-` operator
print(diff_set)  # Output: {1, 2}


diff_set = set1.difference(set2)  # Met `difference()` methode
print(diff_set)  # Output: {1, 2}

#controle of een element in een set zit
print(2 in set1)  # Output: True
print(5 in set1)  # Output: False

#Sets kunnen worden vergeleken met behulp van:

#  == (Gelijke sets)
# issubset() (Onderdeel van een andere set)
#`issuperset() (Bevat een andere set)

set3 = {1, 2}
set4 = {1, 2, 3, 4}

print(set3.issubset(set4))  # True, want {1, 2} zit in {1, 2, 3, 4}
print(set4.issuperset(set3))  # True, want {1, 2, 3, 4} bevat {1, 2}



