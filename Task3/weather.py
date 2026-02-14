import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "8c8e3ccc415124f7c3c4a9b65719db7e"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = ( 
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        condition = data["weather"][0]["description"].title()

        result_label.config(
            text=(
                f"🌍 City: {city.title()}\n\n"
                f"🌡 Temperature: {temp} °C\n"
                f"☁ Condition: {condition}\n"
                f"💧 Humidity: {humidity}%\n"
                f"🌬 Wind Speed: {wind} m/s"
            )
        )

    except Exception:
        messagebox.showerror("Error", "Unable to fetch weather data")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Weather App")
root.state('zoomed')
root.configure(bg="#1e3d59")

title = tk.Label(
    root,
    text="Weather Application",
    font=("Helvetica", 18, "bold"),
    bg="#1e3d59",
    fg="white"
)
title.pack(pady=15)

city_entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

get_button = tk.Button(
    root,
    text="Get Weather",
    font=("Helvetica", 12, "bold"),
    bg="#f5a623",
    fg="black",
    command=get_weather
)
get_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 12),
    bg="#1e3d59",
    fg="white",
    justify="left"
)
result_label.pack(pady=20)

root.mainloop()
