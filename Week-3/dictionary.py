#dictionary - Object
#ongeordende, veranderlijke (mutable) verzameling van KEY-VALUE pairs

patient = {
    "name": "Niels",
    "age": 31, 
    "birthplace" : "Bruges",
    "vaccinated" : True
}

print(patient["birthplace"])
print(patient.get("vaccinated"))

print(patient["hospital"]) # zal een error vertonen
print(patient.get("hospital")) # zal 'None' tonen als waarde

#toevoegen 
patient["hospital"] = "Az. St-Lucas"
print(patient)

#verwijderen
del patient["hospital"]
print(patient)

#methoden

#keys()
#values()
#items()
#update()

#keys() (haalt alle keys op)
print(patient.keys())

#values() (haalt alle values op)
print(patient.values())

#items() (haalt zowel de keys als de values op)
print(patient.items())

#update() -> voegt een key-value pair toe aan het object (dictionary)
patient.update({"hobbys": "lui zijn"})
print(patient)