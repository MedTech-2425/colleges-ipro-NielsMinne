def stock_check(item, stock):
    match item:
        case "medicijnen":
            if stock < 50:
                return "Waarschuwing: voorraad medicijnen is laag."
            else:
                return "Voorraad medicijnen is op peil."
        case "verbanden":
            if stock < 100:
                return "Waarschuwing: voorraad verbanden is laag."
            else:
                return "Voorraad verbanden is op peil."
        case "handschoenen":
            if stock < 200:
                return "Waarschuwing: voorraad handschoenen is laag."
            else:
                return "Voorraad handschoenen is op peil."
        case _:
            return "Item niet herkend."

# Voorbeeld:
result = stock_check("medicijnen", 45)
print(result)  # Output: Waarschuwing: voorraad medicijnen is laag.