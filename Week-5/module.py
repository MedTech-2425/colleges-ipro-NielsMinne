import random 
import statistics

# random choice verwacht een lijst van items en zal daaruit 1 kiezen
print(random.choice(["Head","Tails"]))

#random randint zal een getal van x tot y kiezen inclusief
print(random.randint(1,10))

#random shuffle zal de lijst door elkaar schudden
colors = ["blue", "red", "yellow"]
random.shuffle(colors)

for color in colors:
    print(color)

#-----------------------------------------
#Statistics 

#zie documentatie

#mean zal het gemiddelde geven van een lijst van getallen
result = statistics.mean([100,90,50,60])
print(result)
