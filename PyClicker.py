#! python3
from tkinter.constants import  LEFT 
from typing import Text
import keyboard
import pyautogui
import tkinter as tk
root = tk.Tk()

root.attributes('-fullscreen', True, '-alpha',0.5)
root.title("PyClicker")

canvas = tk.Canvas(root, bg="#000000")
canvas.pack(fill=tk.BOTH, expand=True)
frame = tk.Frame(root)

# closeButton = tk.Button(canvas, text="X", command=root.destroy, bg="red", height=1, width=2).grid(column=1, row=10)
quitLabel = tk.Label(frame, text= "press ESC to quit", height=10, width=250, bg = "white")
quitLabel.pack(side=LEFT)
frame.pack()

def quit(event): 
    if(event.keysym == "Escape"): 
        root.destroy()

def motion(event):
    x, y = pyautogui.position()
    print('{}, {}'.format(x, y))

def startClicker(event): 
    x, y = pyautogui.position()
    print("clicked")
    root.withdraw()
    while True: 
        pyautogui.click(x= x, y = y)
        if keyboard.is_pressed('esc'): 
            root.deiconify()
            break
root.bind("<Key>", quit)
root.bind("<ButtonPress-1>", startClicker)
root.mainloop()

