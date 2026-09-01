from calculations import (
    calculate_profit_margin,
    calculate_revenue,
    calculate_yield_per_acre,
    calculate_saleable_weight,
    calculate_profit,
    calculate_total_cost
)

#----- import the farmers data on the screen
print("Cocoa Farmer Assistant")
harvest_weight = float(input("How many kg of cocoa beans were harvested? "))
rejected_weight = float(input("How many kg of cocoa beans were rejected? "))
saleable_weight = calculate_saleable_weight(harvest_weight, rejected_weight)
price = float(input("What is the price per kg of cocoa beans? "))
labour = float(input("What is the total labour cost? "))
transport = float(input("What is the total transport cost? "))
other_costs = float(input("What is the total cost of other inputs? "))
farm_size = float(input("What is the size of the farm in acres? "))

yield_per_acre = calculate_yield_per_acre(saleable_weight, farm_size)
revenue = calculate_revenue(saleable_weight, price)
total_cost = calculate_total_cost(labour, transport, other_costs)
profit = calculate_profit(revenue, total_cost)
profit_margin = calculate_profit_margin(profit, revenue)
print(f"Yield per Acre: {yield_per_acre:.2f} kg/acre")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Total Revenue: ${revenue:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
print(f"Profit: ${profit:.2f}")