import tkinter as tk
from tkinter import ttk, messagebox

from calculations import (
    calculate_profit_margin,
    calculate_profit,
    calculate_total_cost,
    calculate_revenue,
    calculate_yield_per_acre,
    calculate_saleable_weight,
)

from database import get_farm_records, delete_farm_record, save_farm_record
from quality_checks import check_moisture, get_quality_ratings


def start_dashboard():
   

    window = tk.Tk()
    window.title("Cocoa Farmer Assistant")
    window.geometry("900x700")

    title_label = tk.Label(window, text="Cocoa Farm Dashboard", font=("Arial", 16, "bold"))
    title_label.pack(pady=20)
    subtitle_label = tk.Label(window, text="Enter your farm data below:", font=("Arial", 12))
    subtitle_label.pack(pady=10)

    input_frame = tk.LabelFrame(window, text="Farm Data", padding=20)
    input_frame.pack(pady=20, padx=30, fill="x")

    labels = [
        "Harvest Weight (kg):",
        "Rejected Weight (kg):",
        "Price per kg (N):",
        "Labour Cost (N):",
        "Transport Cost (N):",
        "Total Cost of Other Inputs (N):",
        "Farm Size (acres):",
        "Moisture Level (%):"
    ]

    entries = []
    for row, label_text in enumerate(labels):
        label = tk.Label(input_frame, text=label_text)
        label.grid(row=row, column=0, sticky="w", pady=5)
        entry = tk.Entry(input_frame)
        entry.grid(row=row, column=1, pady=5)
        entries.append(entry)
    (harvest_weight_entry, rejected_weight_entry, price_entry, labour_entry, transport_entry, other_costs_entry, farm_size_entry, moisture_entry) = entries

    result_frame = tk.LabelFrame(window, text="Results", padding=20)
    result_frame.pack(pady=20, padx=30, fill="x")

    result_label = tk.Label(result_frame, text="Enter farm data and click 'Calculate' to see results.", font=("Arial", 12, "bold"))
    result_label.pack(pady=10)


def calculate():
    try:
        harvest_weight = float(harvest_weight_entry.get())
        rejected_weight = float(rejected_weight_entry.get())
        price = float(price_entry.get())
        labour = float(labour_entry.get())
        transport = float(transport_entry.get())
        other_costs = float(other_costs_entry.get())
        farm_size = float(farm_size_entry.get())
        moisture = float(moisture_entry.get())


        if harvest_weight <= 0:
           raise ValueError("Harvest weight must be greater than 0." 
            )

        if rejected_weight < 0:
            raise ValueError("Rejected weight must be a non-negative value.")
        
        if price <= 0:
            raise ValueError("Price must be greater than 0."
            )
        
        if labour < 0:
            raise ValueError("Labour cost must be a non-negative value.")
        
        if transport < 0:
            raise ValueError("Transport cost must be a non-negative value.")
        
        if other_costs < 0:
            raise ValueError("Other costs must be a non-negative value."
            )
        
        if farm_size <= 0:
            raise ValueError("Farm size must be greater than 0.")

        if moisture < 0:
            raise ValueError("Moisture level must be a non-negative value.")


#----- perform calculations after validating inputs

        saleable_weight = calculate_saleable_weight(harvest_weight, rejected_weight)
        yield_per_acre = calculate_yield_per_acre(saleable_weight, farm_size)
        revenue = calculate_revenue(saleable_weight, price)
        total_cost = calculate_total_cost(labour, transport, other_costs)
        profit = calculate_profit(revenue, total_cost)
        profit_margin = calculate_profit_margin(profit, revenue)

        quality_check = check_moisture(moisture)

        result = (
            f"Saleable Weight: {saleable_weight:.2f} kg\n"
            f"Yield per Acre: {yield_per_acre:.2f} kg/acre\n"
            f"Revenue: ${revenue:.2f}\n"
            f"Total Cost: ${total_cost:.2f}\n"
            f"Profit: ${profit:.2f}\n"
            f"Profit Margin: {profit_margin:.2f}%\n"
            f"Quality Check: {'Pass' if quality_check else 'Fail'}"
        )
        result_label.config(text=result, fg="blue")#

        save_farm_record(harvest_weight, rejected_weight, price, labour, transport, other_costs, farm_size, moisture)

        messagebox.showinfo("Success", "Farm data saved successfully!")
    except ValueError as error:
        messagebox.showerror("Input Error", str(error))

def view_records():
    records = get_farm_records()
    if not records:
        messagebox.showinfo("No Records", "No farm records found.")
        return

    records_window = ttk.Toplevel(window)
    records_window.title("Farm Records")
    records_window.geometry("800x400")

    tree = ttk.Treeview(records_window, columns=("ID", "Harvest Weight", "Rejected Weight", "Price per kg", "Labour Cost", "Transport Cost", "Other Costs", "Farm Size", "Moisture Level", "Created At"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Harvest Weight", text="Harvest Weight (kg)")
    tree.heading("Rejected Weight", text="Rejected Weight (kg)")
    tree.heading("Price per kg", text="Price per kg (N)")
    tree.heading("Labour Cost", text="Labour Cost (N)")
    tree.heading("Transport Cost", text="Transport Cost (N)")
    tree.heading("Other Costs", text="Other Costs (N)")
    tree.heading("Farm Size", text="Farm Size (acres)")
    tree.heading("Moisture Level", text="Moisture Level (%)")
    tree.heading("Created At", text="Created At")

    for record in records:
        tree.insert("", ttk.END, values=record)

    tree.pack(expand=True, fill=tk.BOTH)

    button_frame = ttk.Frame(records_window)
    button_frame.pack(pady=10)

    calculate_button = ttk.Button(button_frame, text="Calculate Totals")
    calculate_button.grid(row=0, column=0, padx=10)

    records_button = ttk.Button(button_frame, text="View Record", command=lambda: view_selected_record(tree))
    records_button.grid(row=0, column=1, padx=10)

    exit_button = ttk.Button(button_frame, text="Exit", command=records_window.destroy)

window.mainloop()