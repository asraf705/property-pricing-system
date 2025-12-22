def calculate_price(intent, rule):
    price = rule["base_price"]

    if intent["area"] > rule["base_area"]:
        extra_area = intent["area"] - rule["base_area"]
        units = extra_area // rule["per_unit"]
        price += units * rule["per_price"]

    if intent["debris"]:
        price += rule.get("debris", 0)

    return price
