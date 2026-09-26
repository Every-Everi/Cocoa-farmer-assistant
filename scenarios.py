scenarios = [
    {
        "name": "Scenario 1: Ideal Conditions",
        "moisture_level": 7,
        "harvest_weight": 1000,
        "rejected_weight": 100
    },
    {
        "name": "Scenario 2: High Moisture",
        "moisture_level": 12,
        "harvest_weight": 1000,
        "rejected_weight": 100
    },
    {
        "name": "Scenario 3: High Rejection Rate",
        "moisture_level": 8,
        "harvest_weight": 1000,
        "rejected_weight": 200
    }
]

def get_scenarios():
    return scenarios