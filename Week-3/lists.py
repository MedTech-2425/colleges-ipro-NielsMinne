# #List 
# Geordend en veranderlijk (mutable) verzameling van elementen


# Een lijst maken met vierkante haakjes
list_example = [1, 2, 3, 4, 5]
print(list_example)  # Output: [1, 2, 3, 4, 5]

# Een lijst maken met de list() functie
list_example2 = list([1, 2, 3, 4, 5])
print(list_example2)  # Output: [1, 2, 3, 4, 5]

#toegang tot ljist elementen 
print(list_example[1]) #output: 2 -> in programmeren starten we van index 0

print(list_example[-1]) #output: 5

#slicen
sub_list = list_example[1:3]  # Haalt elementen op van index 1 tot en met 2 [beginwaarde, eindwaarde niet inclusief]
print(sub_list)  # Output: [2, 3]

#mergen
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = list1 + list2
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]

#soorten methoden 
#append() -> Voegt een element toe aan het einde van de lijst.
#remove() -> Verwijdert het eerste voorkomen van een element.
#pop() ->Verwijdert het laatste element (of een specifiek index).
#extend() -> Voegt meerdere elementen toe aan een lijst.
#insert()-> Voegt een element op een specifieke index toe.
#sort() -> Sorteert de lijst op plaats.
#reverse() -> Draait de lijst om.

# #append  - .append() -> voeg toe op het einde
list_example = [1, 2, 3]
list_example.append(4)
print(list_example)  # Output: [1, 2, 3, 4]

list_names = ["Milan", "Eline","Eline2", "Igor","Erica"]
list_names.append("Miguel")
print(list_names)

#verwijderen van de lijst - .pop()
list_names.pop()
print(list_names)

#remove - .remove()
list_names.remove("Eline2")
print(list_names)

#extend()
list_names.extend(["Andreas", "Aaron"])
print(list_names)

#insert() 
fruit.insert(2, "Kiwi")
print(fruit)


#sort()
fruit.sort()
print(fruit)

#reverse()
fruit.reverse()
print(fruit)


# #list unpacken -> Van elke item een aparte variabele maken
fruit = ["Apple", "Banaan","Mango","Dragonfruit"]
fruit1 , fruit2, fruit3, fruit4 = fruit

#items overslaan 
fruit1, *other_fruits, fruit4 = fruit
print(fruit1)
print(other_fruits)
print(fruit4)




