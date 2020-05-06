import tkinter as tk


HEIGHT = 700
WIDTH = 800

root = tk.TK()
canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH)
canvas.pack()
# widgets
# frame within the canvas
frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth = 0.8, relheight=0.5)

# key word arguments #
button = tk.Button(frame, text='Test button', bg='gray', fg='red')
button.grid(row=0, column=0)

label = tk.Label(frame, text="This is the label", bg='yellow')
label.grid(row=0, column=1)

entry = tk.Entry(frame, bg='green')
entry.grid(row=0, column=2)
# you can use place, grid, or pack to arrange #

def format_repsonse(weather_json):
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (F): %s' %()


root.mainloop()