#!/usr/bin/env python3
import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a canvas to draw the car
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Draw a complex car divided into 8 sections
sections = []
car_parts = [
    [(100, 200), (100, 200), (250, 200), (550, 200), (600, 300), (700, 300), (700, 400), (100, 400)],  # Body
    [150, 375],  # Wheel
    [500, 375],  # Wheel
    [(200, 300), (400, 300), (400, 220), (200, 220)],  # Window
    [(450, 300), (590, 300), (550, 220), (450, 220)],  # Window
    [(80, 300), (110, 300), (110, 340), (80, 340)],    # Headlight
    [(680, 300), (710, 300), (710, 340), (680, 340)]   # Headlight
]

section_labels = ["Kere", "Tagumine ratas", "Esimene ratas", "Tagumised klaasid", "Esimesed klaasid", "Tagatuled", "Esituled"]
section_colors = ["black", "gray", "gray", "light blue", "light blue", "red", "yellow"]

for i, part in enumerate(car_parts):
    if len(part) == 2:  # Draw wheels as circles
        x, y = part[0], part[1]
        section = canvas.create_oval(x, y, x+150, y+150, fill='', outline='black')
    else:  # Draw other parts as polygons
        section = canvas.create_polygon(part, fill='', outline='black')
    sections.append(section)

# Function to change section color and button color
def change_color(section, color, button):
    canvas.itemconfig(section, fill=color)
    button.config(bg='green', activebackground='green')

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(side='bottom', fill='x')

# Create buttons for each section
buttons = []
for i in range(7):
    button = tk.Button(button_frame, text=section_labels[i], command=lambda i=i: change_color(sections[i], section_colors[i], buttons[i]), font='Helvetica 10 bold')
    button.pack(side='left', expand=True, fill='both')
    buttons.append(button)

# Run the main loop
root.mainloop()
