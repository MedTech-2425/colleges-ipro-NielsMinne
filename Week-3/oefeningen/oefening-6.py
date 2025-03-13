def main():
    patients= [
        {"name" : 'John Doe', "treatment": 'Chemotherapy'},
        {"name" : 'Sarah Doe', "treatment": 'Physical therapy'},
        {"name" : 'Alice Brown', "treatment": 'Radiation therapy'},
    ]

    print_treatments(patients)

def print_treatments(patients: list):
    for patient in patients:
        print(f"{patient['name']} is undergoing {patient['treatment']} ")

if __name__ == "__main__":
    main()