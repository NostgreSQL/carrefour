import tkinter as tk
import time


root = tk.Tk()
root.title("Светофор")
lable = tk.Label()
canvas = tk.Canvas(root, width=100, height=250)


red_light = canvas.create_oval(25, 20, 75, 70, fill="gray")
yellow_light = canvas.create_oval(25, 95, 75, 145, fill="gray")
green_light = canvas.create_oval(25, 170, 75, 220, fill="gray")
canvas.pack()

root.mainloop()
