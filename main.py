from calculations import (
    calculate_profit_margin,
    calculate_revenue,
    calculate_yield_per_acre,
    calculate_saleable_weight,
    calculate_profit,
    calculate_total_cost
)

from database import create_table, get_connection, save_farm_record
from datetime import datetime
from database import get_farm_records
import tkinter as tk


create_table()  # Ensure the database and table are created before saving records

window = tk.Tk()
window.withdraw()

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

# Save the farm record to the database
save_farm_record(harvest_weight, rejected_weight, price, labour, transport, other_costs, farm_size)

records = get_farm_records()
for record in records:
    (record)

# Display the farm records
def show_farm_records():
    records_window = tk.Toplevel(window)
    records_window.title("Farm Records")

    for record in records:
        record_text = str(record)
        record_label = tk.Label(records_window, text=record_text)
        record_label.pack(pady=2)

print(f"Yield per Acre: {yield_per_acre:.2f} kg/acre")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Total Revenue: ${revenue:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
print(f"Profit: ${profit:.2f}")