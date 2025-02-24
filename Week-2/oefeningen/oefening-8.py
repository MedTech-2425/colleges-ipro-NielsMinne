def patient_status(status):
    match status:
        case "opgenomen":
            return "De patiënt is opgenomen."
        case "ontslagen":
            return "De patiënt is ontslagen."
        case "wachtlijst":
            return "De patiënt staat op de wachtlijst."
        case _:
            return "Status onbekend."

# Voorbeeld:
result= patient_status("opgenomen")
print(result)  # Output: De patiënt is opgenomen.

result= patient_status("wachtlijst")
print(result)  # Output: De patiënt staat op de wachtlijst.

result= patient_status("ziekenhuisbed")
print(result)  # Output: Status onbekend.