import tkinter as tk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = "bmi_history.csv"

# ---------- BMI LOGIC ----------
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db"
        elif 18.5 <= bmi < 25:
            category = "Normal"
            color = "#2ecc71"
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = "#f1c40f"
        else:
            category = "Obese"
            color = "#e74c3c"

        result_label.config(
            text=f"BMI: {bmi}\nCategory: {category}",
            fg=color
        )

        save_data(bmi, category)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

# ---------- SAVE DATA ----------
def save_data(bmi, category):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "BMI", "Category"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), bmi, category])

# ---------- SHOW GRAPH ----------
def show_graph():
    if not os.path.exists(FILE_NAME):
        messagebox.showinfo("No Data", "No BMI history found.")
        return

    dates = []
    bmis = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(row["Date"])
            bmis.append(float(row["BMI"]))

    plt.figure(figsize=(8, 4))
    plt.plot(dates, bmis, marker="o")
    plt.xticks(rotation=45, fontsize=8)
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.title("BMI Trend Over Time")
    plt.tight_layout()
    plt.show()

# ---------- GUI ----------
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("420x420")
root.configure(bg="#1e1e2f")

title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="#f39c12"
)
title_label.pack(pady=15)

frame = tk.Frame(root, bg="#2c2c3e", padx=20, pady=20)
frame.pack(pady=10)

tk.Label(frame, text="Weight (kg)", bg="#2c2c3e", fg="white", font=("Arial", 12)).grid(row=0, column=0, pady=10)
weight_entry = tk.Entry(frame, font=("Arial", 12))
weight_entry.grid(row=0, column=1)

tk.Label(frame, text="Height (m)", bg="#2c2c3e", fg="white", font=("Arial", 12)).grid(row=1, column=0, pady=10)
height_entry = tk.Entry(frame, font=("Arial", 12))
height_entry.grid(row=1, column=1)

calc_btn = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12, "bold"),
    bg="#27ae60",
    fg="white",
    command=calculate_bmi,
    width=18
)
calc_btn.pack(pady=15)

result_label = tk.Label(
    root,
    text="BMI: --\nCategory: --",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="white"
)
result_label.pack(pady=10)

graph_btn = tk.Button(
    root,
    text="View BMI History Graph",
    font=("Arial", 11),
    bg="#2980b9",
    fg="white",
    command=show_graph,
    width=22
)
graph_btn.pack(pady=10)

root.mainloop()









