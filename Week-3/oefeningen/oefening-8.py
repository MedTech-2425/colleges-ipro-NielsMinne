def main():
    # Start dictionary met patiëntnamen en hun medische tests
    patient_tests = {
        'John Doe': {'Blood test', 'MRI scan'},
        'Jane Smith': {'ECG', 'X-ray'},
        'Alice Brown': {'Blood test', 'X-ray', 'MRI scan'}
    }

    # Voeg een nieuwe medische test toe voor een patiënt
    add_medical_tests('John Doe', 'ECG', patient_tests)
    add_medical_tests('Jane Smith', 'Blood test', patient_tests)
    add_medical_tests('Alice Brown', 'ECG', patient_tests)

def add_medical_tests(patient: str, test: str, test_dict: dict):
    # Voeg de test toe aan de set van de patiënt
    if patient in test_dict:
        test_dict[patient].add(test)
    else:
        test_dict[patient] = {test}

    # Print de tests voor elke patiënt na de toevoeging
    for patient, tests in test_dict.items():
        print(f"{patient} has undergone the following tests: {tests}")

# Roep de main functie aan
if __name__ == "__main__":
    main()
