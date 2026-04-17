import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("320x130")
window.attributes("-topmost", True)
window.configure(bg="white")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto, relief=FLAT)

label2 = tk.Label(window, text="Pochacco!", bg="white")
label3 = tk.Label(window, bg="aqua", font=3, text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero")

label1.grid(row=1, column=1)
label2.grid(row=1, column=2)
label3.grid(row=2, column=1)

window.mainloop()

#dekinaiiiii