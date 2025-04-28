def main():
    # Lijst van patiënten met naam, leeftijd en diagnose
    patients = [
        ('John Doe', 45, 'Diabetes'),
        ('Jane Smith', 38, 'Hypertension'),
        ('Alice Brown', 60, 'Cancer')
    ]
    
    # Roep de functie aan om de patiëntinformatie af te drukken
    print_patient_info(patients)

def print_patient_info(patients: list):
    # Gebruik een for-loop om door de lijst van patiënten te itereren
    for patient in patients:
        name, age, diagnosis = patient
        print(f"Patient: {name}, Age: {age}, Diagnosis: {diagnosis}")

# Roep de main functie aan
if __name__ == "__main__":
    main()
