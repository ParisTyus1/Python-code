import tkinter as tk
import requests


HEIGHT = 500
WIDTH = 700

def test_function(entry):
        print("This is the entry: ", entry)

## api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_repsonse(weather_json):
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (F): %s' %(name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str

def get_weather(city):
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json

    label['text'] = format_repsonse(weather)


root = tk.TK()
# These are all widgets from the tkinter GUI package #
canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH)
canvas.pack()
# widgets

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 0.1)

# frame within the canvas
frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth = 0.8, relheight=0.5)

entry = tk.Entry(frame, bg='green')
entry.grid(row=0, column=2)

# key word arguments #
button = tk.Button(frame, text='Test button', bg='gray', fg='red')
button.grid(row=0, column=0)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx = 0.7, rely=0.25,relwidth = 0.3)

label = tk.Label(frame, text="This is the label", bg='yellow')
label.grid(row=0, column=1)
# you can use place, grid, or pack to arrange #


root.mainloop()