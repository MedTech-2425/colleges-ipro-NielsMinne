def main():
    patients = ["John Doe", "Jane Smith", "Alice Brown"]
    new_patient = "Bob White"

    updated_patients = add_patient(patients, new_patient)
    print("Updated patienten lijst: ", updated_patients)

def add_patient(patients, new_patient):
    patients.append(new_patient)
    return patients


if __name__ == "__main__":
    main()
