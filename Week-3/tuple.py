#tuple
# Geordend en onveranderlijk (immutable) verzameling van elementen

# Een tuple maken met haakjes
tuple_example = (1, 2, 3, 4, 5)
print(tuple_example)  # Output: (1, 2, 3, 4, 5)

# Een tuple maken met de tuple() functie
tuple_example2 = tuple([1, 2, 3, 4, 5])
print(tuple_example2)  # Output: (1, 2, 3, 4, 5)

#LET OP!
tuple_example = (5,)  # Dit is een tuple
not_a_tuple = (5)  # Dit is een integer

#toegang tot tuple elementen (zelfde als een list)
tuple_example = (10, 20, 30, 40)
print(tuple_example[1])  # Output: 20

#tuple slicing
sub_tuple = tuple_example[1:3]  # Haalt elementen op van index 1 tot en met 2
print(sub_tuple)  # Output: (20, 30)

#tuple samenvoegen en herhalen 
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

merged_tuple = tuple1 + tuple2  # Samenvoegen
print(merged_tuple)  # Output: (1, 2, 3, 4, 5, 6)

repeated_tuple = tuple1 * 2  # Herhalen
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

#Tuple Methoden 
#count() -> Telt hoe vaak een waarde voorkomt.
#index() -> Geeft de index van de eerste keer dat een waarde voorkomt.

tuple_example = (1, 2, 3, 2, 4, 2)
print(tuple_example.count(2))  # Output: 3
print(tuple_example.index(3))  # Output: 2

#unpacken van een tuple 
tuple_example = ("apple", "banana", "cherry")
fruit1, fruit2, fruit3 = tuple_example
print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry
