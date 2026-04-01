import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("100x600")
window.attributes("-topmost", True)

entry1 = tk.Entry(window, width=10)
label1 = tk.Label(window, text="x")
entry2 = tk.Entry(window, width=10)
label2 = tk.Label(window, text="=")
entry3 = tk.Entry(window, width=20)

entry1.grid(row=1, column=1)
label1.grid(row=1, column=2)
entry2.grid(row=1, column=3)
label2.grid(row=1, column=4)
entry3.grid(row=1, column=5)

window.mainloop()
