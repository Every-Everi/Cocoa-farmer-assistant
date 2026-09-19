import tkinter as tk
from tkinter import ttk, messagebox

from calculations import (
    calculate_profit_margin,
    calculate_revenue,
    calculate_yield_per_acre,
    calculate_saleable_weight,
    calculate_profit,
    calculate_total_cost
)

from database import create_table, get_connection, save_farm_record, get_farm_records


create_table()  # Ensure the database and table are created before saving records

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
    print(record)

# Display the farm records
def show_farm_records():
    records = get_farm_records()
    if not records:
        messagebox.showinfo("Farm Records", "No farm records found.")
        return
    for record in records:
        print(record)
def add_farm_record():
    try:
        harvest_weight = float(input("How many kg of cocoa beans were harvested? "))
        rejected_weight = float(input("How many kg of cocoa beans were rejected? "))
        price = float(input("What is the price per kg of cocoa beans? "))
        labour = float(input("What is the total labour cost? "))
        transport = float(input("What is the total transport cost? "))
        other_costs = float(input("What is the total cost of other inputs? "))
        farm_size = float(input("What is the size of the farm in acres? "))

        if harvest_weight <= 0:
            print("Harvest weight must be greater than 0.")
            return
        if rejected_weight < 0:
            print("Rejected weight cannot be negative.")
            return#
        if rejected_weight > harvest_weight:
            print("Rejected weight cannot be greater than harvest weight.")
            return
        if price <= 0:
            print("Price per kg must be greater than 0.")
            return
        if labour < 0:
            print("Labour cost cannot be negative.")
            return
        if transport < 0:
            print("Transport cost cannot be negative.")
            return
        if other_costs < 0:
            print("Other costs cannot be negative.")
            return
        if farm_size <= 0:
            print("Farm size must be greater than 0.")
            return

        saleable_weight = calculate_saleable_weight(harvest_weight, rejected_weight)
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

        # Save the farm record to the database
        save_farm_record(harvest_weight, rejected_weight, price, labour, transport, other_costs, farm_size)

        print("Farm record added successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric values for weights, costs, and farm size.")

#----- main menu
def main():
    while True:
        print("\n--- Farm Record Management ---")
        print("1. Add Farm Record")
        print("2. Show Farm Records")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_farm_record()
        elif choice == "2":
            show_farm_records()
        elif choice == "3":
            print("Exiting..., thank you for choosing the Cocoa Farmer Assistant.")
            break
        else:
            print("Invalid option. Please select 1, 2 or 3.")

if __name__ == "__main__":
    main()