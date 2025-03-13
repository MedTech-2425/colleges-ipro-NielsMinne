def main():
    devices = {'X-ray machine': 'In use', 'MRI scanner': 'Available'}
    updated_devices = update_devices_status('MRI scanner', 'Kapot', devices )
    print(updated_devices)

def update_devices_status(device ,status ,devices):
    devices[device] = status
    return devices


if __name__ == "__main__":
    main()