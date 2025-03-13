def main():
    devices = ["MRI Scanner", "X-ray machine", "Ultrasound"]
    new_device = input("Welke device wil je toevoegen? ")

    try:
        updated_devices = add_medical_device(devices, new_device)
        print("Updated device list: ", updated_devices)
    except ValueError as e:
        print(e)


def add_medical_device(devices, new_device):
    """Voegt een medisch apparaat toe als het nog niet in de lijst staat"""

    if new_device in devices:
        raise ValueError(f"{new_device} is al in de lijst")
    devices.append(new_device)
    return devices


if __name__ == "__main__":
    main()
