import tkinter as tk
from tkinter import font
from calculations import (
    calculate_profit_margin,
    calculate_profit,
    calculate_total_cost,
    calculate_revenue,
    calculate_yield_per_acre,
    calculate_saleable_weight,
)

window = tk.Tk()
window.title("Cocoa Farmer Assistant")
window.geometry("400x700")

def oncalculate():
    try:
        harvest_weight = float(harvest_weight_entry.get())
        rejected_weight = float(rejected_weight_entry.get())
        price = float(price_entry.get())
        labour = float(labour_entry.get())
        transport = float(transport_entry.get())
        other_costs = float(other_costs_entry.get())
        farm_size = float(farm_size_entry.get())


        if harvest_weight <= 0:
            warning_label.config(
                text="Harvest weight must be greater than 0.",
                fg="red"
            )
            return
        if rejected_weight < 0:
            warning_label.config(
                text="Rejected weight must be a non-negative value.",
                fg="red"
            )
            return
        if price <= 0:
            warning_label.config(
                text="Price must be greater than 0.",
                fg="red"
            )
            return
        if labour < 0:
            warning_label.config(
                text="Labour cost must be a non-negative value.",
                fg="red"
            )
            return
        if transport < 0:
            warning_label.config(
                text="Transport cost must be a non-negative value.",
                fg="red"
            )
            return
        if other_costs < 0:
            warning_label.config(
                text="Other costs must be a non-negative value.",
                fg="red"
            )
            return
        if farm_size <= 0:
            warning_label.config(
                text="Farm size must be greater than 0.",
                fg="red"
            )
            return

#----- perform calculations after validating inputs

        saleable_weight = calculate_saleable_weight(harvest_weight, rejected_weight)
        yield_per_acre = calculate_yield_per_acre(saleable_weight, farm_size)
        revenue = calculate_revenue(saleable_weight, price)
        total_cost = calculate_total_cost(labour, transport, other_costs)
        profit = calculate_profit(revenue, total_cost)
        profit_margin = calculate_profit_margin(profit, revenue)

        #----- display the results in the entry fields and result label
        yield_per_acre_entry.delete(0, tk.END)
        yield_per_acre_entry.insert(0, f"{yield_per_acre:.2f}")

        profit_margin_entry.delete(0, tk.END)
        profit_margin_entry.insert(0, f"{profit_margin:.2f}")

        result_label.config(text=f"Saleable Weight: {saleable_weight:.2f} kg\nRevenue: ${revenue:.2f}\nTotal Cost: ${total_cost:.2f}\nProfit: ${profit:.2f}", fg="blue")

        if moisture_entry.get():
            moisture = float(moisture_entry.get())
            if moisture > 8:
                warning_label.config(text="Warning: Moisture level is above 8%!", fg="red")
            else:
                warning_label.config(text="Moisture level is acceptable.", fg="green")

        if profit_margin < 0:
            warning_label.config(text="Warning: Profit margin is negative!", fg="red")
        else:
            warning_label.config(text="Profit margin is positive.", fg="green")

        if harvest_weight > 0 and rejected_weight > (harvest_weight * 0.15):
            warning_label.config(text="Warning: Rejected weight is more than 15% of harvest weight!", fg="red")
        else:
            warning_label.config(text="Rejected weight is within acceptable limits.", fg="green")

    except ValueError:
        warning_label.config(text="Error: Please enter valid numeric values.", fg="red")    


#----- add a title label to the window
title_label = tk.Label(window, text="Cocoa Farm Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

#----- add harvest weight label and entry field to the window
harvest_weight_label = tk.Label(window, text="Harvest Weight (kg):")
harvest_weight_label.pack()
harvest_weight_entry = tk.Entry(window)
harvest_weight_entry.pack(pady=10)

#----- add a price per kg label and entry field to the window
price_label = tk.Label(window, text="Price per kg ($):")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack(pady=10)

#----- add a labour cost label and entry field to the window
labour_label = tk.Label(window, text="Labour Cost ($):")
labour_label.pack()
labour_entry = tk.Entry(window)
labour_entry.pack(pady=10)

#----- add a transport cost label and entry field to the window
transport_label = tk.Label(window, text="Transport Cost ($):")
transport_label.pack()
transport_entry = tk.Entry(window)
transport_entry.pack(pady=10)

#----- add a total cost of other inputs label and entry field to the window
other_costs_label = tk.Label(window, text="Total Cost of Other Inputs ($):")
other_costs_label.pack()
other_costs_entry = tk.Entry(window)
other_costs_entry.pack(pady=10)

#----- add a farm size label and entry field to the window
farm_size_label = tk.Label(window, text="Farm Size (acres):")   
farm_size_label.pack()
farm_size_entry = tk.Entry(window)
farm_size_entry.pack(pady=10)

#----- add a rejected weight label and entry field to the window
rejected_weight_label = tk.Label(window, text="Rejected Weight (kg):")
rejected_weight_label.pack()
rejected_weight_entry = tk.Entry(window)
rejected_weight_entry.pack(pady=10)

#----- add a yield per acre label to the window
yield_per_acre_label = tk.Label(window, text="Yield per Acre (kg/acre):")
yield_per_acre_label.pack(pady=10)
yield_per_acre_entry = tk.Entry(window)
yield_per_acre_entry.pack(pady=10)

#---- add a moisture label and entry field to the window
moisture_label = tk.Label(window, text="Moisture Level (%):")
moisture_label.pack()
moisture_entry = tk.Entry(window)
moisture_entry.pack(pady=10)

#----- add a profit margin label to the window
profit_margin_label = tk.Label(window, text="Profit Margin (%):")
profit_margin_label.pack()
profit_margin_entry = tk.Entry(window)
profit_margin_entry.pack(pady=10)

#----- add a result label to the window
result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)



warning_label = tk.Label(window, text="", font=("Arial", 10, "bold"))  # Add some space before the button
warning_label.pack(pady=15)

#----- add a calculate button to the window
calculate_button = tk.Button(window, text="Calculate", command=oncalculate)
calculate_button.pack(pady=20)

window.mainloop()