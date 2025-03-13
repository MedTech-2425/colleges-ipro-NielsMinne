def main():
    patient_1_diagnoses = ["Diabetes", "Hypertension", "Asthma"]
    patient_2_diagnoses = ["Cancer", "Anemia", "Fatigue"]

    print(store_diagnoses(patient_1_diagnoses))
    print(store_diagnoses(patient_2_diagnoses))

def store_diagnoses(diagnoses):
    return tuple(diagnoses)

if __name__ == "__main__":
    main()