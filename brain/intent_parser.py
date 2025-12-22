def parse_intent(service, area, debris):
    return {
        "service": service.strip().lower(),
        "area": int(area),
        "debris": debris
    }
