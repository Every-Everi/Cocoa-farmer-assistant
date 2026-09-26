def calculate_revenue(saleable_weight, price):
    return saleable_weight * price

def calculate_total_cost(labour, transport, other_costs):
    return labour + transport + other_costs

def calculate_profit(revenue, total_cost):
    return revenue - total_cost

def calculate_saleable_weight(harvest_weight, rejected_weight):
    if harvest_weight < 0:
        raise ValueError("Harvest weight must be not be negative.")
    if rejected_weight < 0:
        raise ValueError("Rejected weight must be not be negative.")
    if rejected_weight > harvest_weight:
        raise ValueError("Rejected weight cannot be greater than harvest weight.")
    return harvest_weight - rejected_weight

def calculate_yield_per_acre(saleable_weight, farm_size):
    if farm_size <= 0:
        raise ValueError("Farm size must be greater than zero.")
    return saleable_weight / farm_size

def calculate_profit_margin(profit, revenue):
    if revenue <= 0:
       return 0
    return (profit / revenue) * 100
