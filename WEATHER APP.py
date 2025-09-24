import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "a33864cab98300a08fde5fbcda693585"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data.get("cod") == 200:  # Success
        main = data["main"]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_desc = data["weather"][0]["description"]

        result = (f"Temperature: {temp}°C\n"
                  f"Pressure: {pressure} hPa\n"
                  f"Humidity: {humidity}%\n"
                  f"Condition: {weather_desc.title()}")
        weather_label.config(text=result)
    else:
        messagebox.showerror("Error", f"City not found or invalid API key.\n\nDetails: {data.get('message')}")



root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

city_label = tk.Label(root, text="Enter City:", font=("Arial", 12))
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=25, font=("Arial", 12))
city_entry.pack(pady=5)

get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
get_weather_btn.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
weather_label.pack(pady=20)

root.mainloop()
