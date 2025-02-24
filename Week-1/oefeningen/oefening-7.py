lengte = float(input("Wat is je lengte in meter? "))
gewicht = float(input("Wat is je gewicht in kg? "))
bmi = gewicht / (lengte ** 2)

print(f"Je BMI is: {round(bmi, 1)}")
print(f"Je BMI is: {bmi:.1f}")