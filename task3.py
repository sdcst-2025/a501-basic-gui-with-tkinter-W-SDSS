import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Example")
window.geometry("260x135")
window.attributes("-topmost", True)
window.configure(bg="white")

dogphoto = PhotoImage(file="dog.png")
f = tk.Frame(window, bg="white")
label1 = tk.Label(f, image=dogphoto, relief=FLAT)
label2 = tk.Label(f, text="Pochacco!", bg="white")
f.pack()
label1.pack(side=LEFT)
label2.pack(side=LEFT)

label3 = tk.Label(window, bg="aqua", text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero")
label3.pack()


window.mainloop()