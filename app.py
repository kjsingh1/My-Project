import requests
import tkinter as tk
from PIL import Image, ImageTk

bg_image = None

def get_weather(event):
    global bg_image 

    user_input = city_entry.get()
    weather_data = requests.get(
        f"http://api.weatherapi.com/v1/forecast.json?key=54f825b8833141e0932183100232212&q={user_input}&days=7"
    )

    if weather_data.status_code == 200:
        weather = weather_data.json().get('current', {}).get('condition', {}).get('text', '').lower()
        temp = round(weather_data.json().get('current', {}).get('temp_f'))

        print(f"Weather: {weather}")
        city_result.config(text=f"The weather in {user_input} is {weather}\ntemperature is {temp}°f")
        
        if "cloud" in weather:
            image = Image.open("Image1.jpeg")
        elif "clear" in weather:
            print("Clear weather")
            image = Image.open("Image.jpeg")
        else:
            image = Image.open("default_image.jpeg")

        bg_image = ImageTk.PhotoImage(image)  

        canvas.delete("all") 
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)  

    else:
        city_result.config(text="Invalid City")

root = tk.Tk()
root.title("Weather By Karamjot Singh")
root.geometry("250x450")

city_label = tk.Label(root, text="Enter a city:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=10)
city_entry.bind("<Return>", lambda event: get_weather(event))

city_result = tk.Label(root, text="")
city_result.pack(pady=10)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

root.mainloop()
