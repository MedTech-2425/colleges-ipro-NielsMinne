def check_alarm(spo2, heart_rate):
    if spo2 < 92 or heart_rate > 120:
        return "ALARM! Zuurstofsaturatie te laag!"
    else:
        return "Geen alarm, alles is normaal."

# Vraag de gebruiker om hun zuurstofsaturatie en hartslag
spo2 = float(input("Voer uw zuurstofsaturatie in (%): "))
heart_rate = int(input("Voer uw hartslag in (bpm): "))

# Controleer of er een alarm is en print het resultaat
alarm_message = check_alarm(spo2, heart_rate)
print(alarm_message)