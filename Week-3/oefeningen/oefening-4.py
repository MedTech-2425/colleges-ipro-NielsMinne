def main():
    tests = ['X-ray', 'Blood test', 'MRI scan', 'X-ray', 'ECG']
    unique = unique_sets(tests)
    print("Unique medical test:", unique)

def unique_sets(tests):
    return set(tests)

if __name__ == "__main__":
    main()