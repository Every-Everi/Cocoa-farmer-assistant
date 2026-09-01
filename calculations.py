def calculate_revenue(harvest_weight, price):
    return harvest_weight * price

def calculate_total_cost(labour, transport, input):
    return labour + transport + input

def calculate_profit(revenue, total_cost):
    return revenue - total_cost

def calculate_saleable_weight(harvest_weight, rejected_weight):
    return harvest_weight - rejected_weight

def calculate_yield_per_acre(saleable_weight, farm_size):
    if farm_size <= 0:
        raise ValueError("Farm size must be greater than zero.")
    return saleable_weight / farm_size

def calculate_profit_margin(profit, revenue):
    if revenue <= 0:
       return 0
    return (profit / revenue) * 100
